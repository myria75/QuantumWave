
"""Main executable of the project
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

import ast
import configparser
from datetime import datetime, date
import time
from src.business.controller.Qiskit_QCSR_Conversor.EmptyCircuitException import EmptyCircuitException
from src.business.controller.Qiskit_QCSR_Conversor.VariableNotCalculatedException import VariableNotCalculatedException
from src.business.controller.Qiskit_QCSR_Conversor.OperationNotFoundException import OperationNotFoundException
import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
import src.business.controller.QmetricsAPI.qmetrics_functions as qmetrics
import src.business.controller.QCPDTool.views as qcpdtool
from src.persistency.Mongo_Ingest_Data_Dealing.languages_ingest_with_dates import doIngestion
from table_information import generateCSV
import io
import os
import json
import logging
import traceback
jsonPath = os.path.join('progress_temp.json')
configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

ingest_logger = logging.getLogger('ingest_logger')
log_capture_string:io.StringIO = io.StringIO() #variable que contiene los logs. Hay que hacer .getvalue()
logger_format_str = "%(asctime)s [%(levelname)s] %(message)s"


if not ingest_logger.hasHandlers():
    ingest_logger.root.handlers=[]
    ingest_logger.basicConfig(
        level=logging.DEBUG,
        format=logger_format_str,
        handlers=[
            logging.FileHandler(eval(config.get('log', 'file'))),
            logging.StreamHandler(log_capture_string)
        ],
        encoding="UTF-8"
    )
else:
    stream_handler = logging.StreamHandler(log_capture_string)
    stream_handler.setFormatter(logging.Formatter(logger_format_str))
    ingest_logger.handlers.extend([
        logging.FileHandler(eval(config.get('log', 'file'))),
        stream_handler
    ])
ingestProgress = 0
analysisProgress = 0

def mainIngestion(languages:list, from_date: date, to_date: date):
    #Ejemplo languages: ["qiskit", "openqasm"]
    if (languages == None or len(languages) == 0): 
        return
    
    ingest_logger.info("THE INGESTION DATA HAS BEGUN!")

    #Searches in GitHub and ingest the data
    doIngestion(languages, from_date, to_date)

    ingest_logger.info("CREATING AST, QUANTUM CIRCUITS IN RQCR FORMAT, METRICS AND PATTERNS!")
    #Searches in db for codes in qiskit language
    from pymongo import MongoClient
    from pymongo import cursor

    db_link = eval(config.get('MongoDB', 'db_link'))
    db_name = eval(config.get('MongoDB', 'db_name'))
    db_coll_final = eval(config.get('MongoDB', 'db_coll_accepted'))
    db_coll_sufix = eval(config.get('MongoDB', 'db_coll_inprogress_sufix'))
    db_coll = (f'{db_coll_final}{db_coll_sufix}')
    connection = MongoClient(db_link, socketTimeoutMS=None)
    dbGithub = connection[db_name]
    collRepo = dbGithub[db_coll]

    query = {}
    documents: cursor.Cursor = collRepo.find(query, no_cursor_timeout=True)
    refreshTime = 600 #10 minutes
    startQueryTime = time.time()

    total_documents = collRepo.count_documents(query)

    with open(jsonPath, 'w+') as file:
        jsonProgress = json.load(file)
    
        jsonProgress['totalFiles_analysis'] = total_documents+1 #+1 por el paso del csv que queda a parte de analizar

        json.dump(jsonProgress, file, indent=4) 

    progress_document = 0

    for document in documents:
        nowQueryTime = time.time()
        if nowQueryTime - startQueryTime >= refreshTime:
            documents.close()
            documents = collRepo.find(query, no_cursor_timeout=True)
            startQueryTime = nowQueryTime

        print(document["path"])
        #ast of the codes and conversion from python qiskit to QCSR
        circuitsJsons = {}
        tree = ""
        try:
            tree = conversor.generateTree(document["content"], document["language"])
        except (IndentationError, Exception):
            continue
        
        errorsFoundAtParse = False
        errorMsg = ""

        try:
            circuitsJsons = conversor.visitTree(tree, document["language"])
        except EmptyCircuitException as e:
            print("Empty array error because QuantumRegister isn't called")
            ingest_logger.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} Empty array error because QuantumRegister isn't called")
            errorsFoundAtParse = True
            errorMsg = "The tree couldn't be generated. Empty array error because QuantumRegister isn't called"
        except VariableNotCalculatedException as e:
            print("A variable during the QCSR circuit conversion couldn't be obtained")
            ingest_logger.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} A variable during the QCSR circuit conversion couldn't be obtained")
            errorsFoundAtParse = True
            errorMsg = f"The ast tree couldn't be generated. A variable during the QCSR circuit conversion couldn't be obtained"
        except ValueError as e:
            print("Translator can't read variables when reading gates/circuit, the code is incompatible")
            ingest_logger.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} Translator can't read variables when reading gates/circuit, the code is incompatible")
            errorsFoundAtParse = True
            errorMsg = f"The ast tree couldn't be generated. Translator can't read variables when reading gates/circuit, the code is incompatible\n{traceback.format_exc()}"
        except (AttributeError, KeyError, IndexError, TypeError, OperationNotFoundException, ZeroDivisionError, Exception) as e: 
            print("-------Throws an error----------")
            print(f"{e.__str__()} {document['path']}")
            ingest_logger.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} throws an error")
            errorsFoundAtParse = True
            errorMsg = f"The tree couldn't be generated. The circuit isn't converted\n{traceback.format_exc()}"

        #TODO: insert general error

        document["circuits"] = []

        for circuit_id, circuit in circuitsJsons.items():
            circuitProperties = {}
            circuitProperties["name"] = circuit_id 
            circuitProperties["circuit"] = circuit
            print(document["path"])
            print(circuit)
            
            qmetricsjson =  {
                "name" : "MiriamTFGCircuit",
                "circuitCode" : circuit
            }

            #Query QPainter and QMetrics 
            qmetrics.updateCircuit(qmetricsjson)
            r = qmetrics.calculateMetrics(qmetricsjson)
            metrics = r.json()

            #Checks if the metrics are correct
            if "status" in metrics:
            #if status starts by 4** or 5**
                if str(metrics["status"])[0] in ("4","5"):
                    ingest_logger.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} QMetrics couldn't calculate the metrics")
                    circuitProperties["metrics"] = { 'error': "QMetrics couldn't calculate the metrics" }
            else: 
                circuitProperties["metrics"] = metrics
                
            circuitProperties["patterns"] = qcpdtool.generate_pattern(circuit)
            document["circuits"].append(circuitProperties)
        
        #Update entry in MongoDB  
        collRepo.update_one({"id": document["id"]},
        {
            "$set": {
                "circuits": document["circuits"]
            }
        })
        progress_document+=1

        with open(jsonPath, 'w+') as file:
            jsonProgress = json.load(file)
        
            jsonProgress['analyzedFiles'] = progress_document

            json.dump(jsonProgress, file, indent=4) 

    dbGithub[db_coll].rename(db_coll_final)

    connection.close()

    generateCSV()

    progress_document+=1

    with open(jsonPath, 'w+') as file:
        jsonProgress = json.load(file)
        
        jsonProgress['analyzedFiles'] = progress_document

        json.dump(jsonProgress, file, indent=4) 