
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
import io
import os
import json
import logging
import traceback

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

log_capture_string = io.StringIO() #variable que contiene los logs. Hay que hacer .getValue()

logging.root.handlers=[]
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(eval(config.get('log', 'file'))),
        logging.StreamHandler(log_capture_string)
    ],
    encoding="UTF-8"
)

def mainExecution(languages, from_date: date, to_date: date):
    #Ejemplo languages: ["qiskit", "openqasm"]
    if (len(languages) == 0): 
        return

    logging.info("--EXCUTION STARTED")
    logging.info("--INGEST STARTED")

    #Searches in GitHub and ingest the data
    doIngestion(languages, from_date, to_date)

    logging.info("--AST, QCSR CIRCUIT, METRICS AND PATTERNS CREATION")
    #Searches in db for codes in qiskit language
    from pymongo import MongoClient
    from pymongo import cursor

    db_link = eval(config.get('MongoDB', 'db_link'))
    db_name = eval(config.get('MongoDB', 'db_name'))
    db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))
    connection = MongoClient(db_link, socketTimeoutMS=None)
    dbGithub = connection[db_name]
    collRepo = dbGithub[db_coll]

    query = {}
    documents: cursor.Cursor = collRepo.find(query, no_cursor_timeout=True)
    refreshTime = 600 #10 minutes
    startQueryTime = time.time()

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
            logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} Empty array error because QuantumRegister isn't called")
            errorsFoundAtParse = True
            errorMsg = "The tree couldn't be generated. Empty array error because QuantumRegister isn't called"
        except VariableNotCalculatedException as e:
            print("A variable during the QCSR circuit conversion couldn't be obtained")
            logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} A variable during the QCSR circuit conversion couldn't be obtained")
            errorsFoundAtParse = True
            errorMsg = f"The ast tree couldn't be generated. A variable during the QCSR circuit conversion couldn't be obtained"
        except ValueError as e:
            print("Translator can't read variables when reading gates/circuit, the code is incompatible")
            logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} Translator can't read variables when reading gates/circuit, the code is incompatible")
            errorsFoundAtParse = True
            errorMsg = f"The ast tree couldn't be generated. Translator can't read variables when reading gates/circuit, the code is incompatible\n{traceback.format_exc()}"
        except (AttributeError, KeyError, IndexError, TypeError, OperationNotFoundException, ZeroDivisionError, Exception) as e: 
            print("-------Throws an error----------")
            print(f"{e.__str__()} {document['path']}")
            logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} throws an error")
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
                    logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} QMetrics couldn't calculate the metrics")
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

    connection.close()
