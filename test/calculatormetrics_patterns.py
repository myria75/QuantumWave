from src.presentation.frontend.metricsPrueba import metricsPrueba
import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
from pymongo import MongoClient
from pymongo import cursor
import time
import os
import configparser
from src.business.controller.Qiskit_QCSR_Conversor.EmptyCircuitException import EmptyCircuitException
from src.business.controller.Qiskit_QCSR_Conversor.VariableNotCalculatedException import VariableNotCalculatedException
from src.business.controller.Qiskit_QCSR_Conversor.OperationNotFoundException import OperationNotFoundException
import logging
import traceback
import io

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll_final = eval(config.get('MongoDB', 'db_coll_accepted'))
db_coll_sufix = eval(config.get('MongoDB', 'db_coll_inprogress_sufix'))
db_coll = (f'{db_coll_final}{db_coll_sufix}')
connection = MongoClient(db_link, socketTimeoutMS=None)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]
ingest_logger = logging.getLogger('ingest_logger')
log_capture_string:io.StringIO = io.StringIO() #variable que contiene los logs. Hay que hacer .getvalue()
logger_format_str = "%(message)s"

query = {}
documents: cursor.Cursor = collRepo.find(query, no_cursor_timeout=True)
refreshTime = 600 #10 minutes
startQueryTime = time.time()

total_documents = collRepo.count_documents(query)

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
        ingest_logger.warning(f"The {document['path']} from {document['name']} repository of {document['author']} (in {document['language']} with {document['extension']} extension), contains an empty array error because QuantumRegister isn't called")
        errorsFoundAtParse = True
        errorMsg = "The tree couldn't be generated. Empty array error because QuantumRegister isn't called"
    except VariableNotCalculatedException as e:
        print("A variable during the QCSR circuit conversion couldn't be obtained")
        ingest_logger.warning(f"The {document['path']} from {document['name']} repository of {document['author']} (in {document['language']} with {document['extension']} extension), contains a variable that couldn't be obtained during the QCSR circuit conversion")
        errorsFoundAtParse = True
        errorMsg = f"The ast tree couldn't be generated. A variable during the QCSR circuit conversion couldn't be obtained"
    except ValueError as e:
        print("Translator can't read variables when reading gates/circuit, the code is incompatible")
        ingest_logger.warning(f"The translator can't read variables when reading gates or circuit in {document['path']} from {document['name']} repository of {document['author']} (in {document['language']} with {document['extension']} extension), so, the code is incompatible")
        errorsFoundAtParse = True
        errorMsg = f"The ast tree couldn't be generated. Translator can't read variables when reading gates/circuit, the code is incompatible\n{traceback.format_exc()}"
    except (AttributeError, KeyError, IndexError, TypeError, OperationNotFoundException, ZeroDivisionError, Exception) as e: 
        print("-------Throws an error----------")
        print(f"{e.__str__()} {document['path']}")
        ingest_logger.warning(f"The {document['path']} from {document['name']} repository of {document['author']} (in {document['language']} with {document['extension']} extension), throws an error")
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

metricsPrueba()