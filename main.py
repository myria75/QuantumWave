
"""Main executable of the project
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

import configparser
from datetime import datetime
from src.business.controller.Qiskit_QCSR_Conversor.EmptyCircuitException import EmptyCircuitException
import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
import src.business.controller.QmetricsAPI.qmetrics_functions as qmetrics
import src.business.controller.QCPDTool.views as qcpdtool
import os
import json
import logging

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

logging.root.handlers=[]
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(eval(config.get('log', 'file')))
        #,logging.StreamHandler()
    ]
)
logging.info("--EXCUTION STARTED")
logging.info("--INGEST STARTED")
#Searches in GitHub and ingest the data
#import src.persistency.Mongo_Ingest_Data_Dealing.languages_ingest_with_dates

logging.info("--CONVERSION STARTED")
#Conversion from base64 to natural language and clasifies into languages and into quantic code and not quantic code
#import src.persistency.Mongo_Ingest_Data_Dealing.conversion

logging.info("--ANTLR4, QCSR CIRCUIT, METRICS AND PATTERNS CREATION")
#Searches in db for codes in qiskit language
from pymongo import MongoClient

db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]

query = {"language": "openqasm"}
documents = collRepo.find(query)

for document in documents:
    print(document["path"])
    #antlr4 of the codes and conversion from python qiskit to QCSR
    circuitJson = ""
    antlr_tree = conversor.generateTree(document["content"], document["language"])
    
    errorsFoundAtParse = False
    errorMsg = ""

    try:
        circuitJson = conversor.deepSearch(antlr_tree, document["language"])
    except EmptyCircuitException as e:
        print("Empty array error because QuantumRegister isn't called")
        logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} Empty array error because QuantumRegister isn't called")
        errorsFoundAtParse = True
        errorMsg = "The antlr4 tree couldn't be generated. Empty array error because QuantumRegister isn't called"
    except ValueError as e:
        print("Translator can't read variables when reading gates/circuit, the code is incompatible")
        logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} Translator can't read variables when reading gates/circuit, the code is incompatible")
        errorsFoundAtParse = True
        errorMsg = "The antlr4 tree couldn't be generated. Translator can't read variables when reading gates/circuit, the code is incompatible"
    except (AttributeError, KeyError, IndexError) as e: 
        print("Throws an error")
        logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} throws an error")
        errorsFoundAtParse = True
        errorMsg = "The antlr4 tree couldn't be generated. The circuit isn't converted"

    if errorsFoundAtParse:
        logging.critical(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} The antlr4 tree couldn't be generated. The circuit isn't converted")
        document["circuit"] = { 'error': errorMsg }
        document["metrics"] = { 'error': errorMsg }
    else:
        document["circuit"] = circuitJson
        print(circuitJson)
        qmetricsjson =  {
            "name" : "MiriamTFGCircuit",
            "circuitCode" : circuitJson
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
                document["metrics"] = { 'error': "QMetrics couldn't calculate the metrics" }
        else: 
            document["metrics"] = metrics

    document["patterns"] = qcpdtool.generate_pattern(circuitJson)
    
    if 'err_msg' in document["patterns"].keys():
        logging.warning(f"{document['language']}.{document['extension']}, {document['author']}/{document['name']} | {document['path']} {document['patterns']['err_msg']}")
    
    #Update entry in MongoDB  
    collRepo.update_one({"id": document["id"]},
    {
        "$set": {
            "circuit": document["circuit"],
            "metrics": document["metrics"],
            "patterns": document["patterns"]
        }
    })

connection.close()