import configparser
from datetime import datetime
import time
from src.business.controller.Qiskit_QCSR_Conversor.EmptyCircuitException import EmptyCircuitException
import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
import src.business.controller.QmetricsAPI.qmetrics_functions as qmetrics
import src.business.controller.QCPDTool.views as qcpdtool
import os
import json
import logging
import traceback
import re

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)


from pymongo import MongoClient
from pymongo import cursor

db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))
connection = MongoClient(db_link, socketTimeoutMS=None)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]

query = {"language": "Python"}
documents: cursor.Cursor = collRepo.find(query, no_cursor_timeout=True)
refreshTime = 600 #10 minutes
startQueryTime = time.time()
counterErrorCircuit = 0
counterCircuit = 0


errors_dict = {}

for document in documents:
    
    
    nowQueryTime = time.time()
    if nowQueryTime - startQueryTime >= refreshTime:
        documents.close()
        documents = collRepo.find(query, no_cursor_timeout=True)
        startQueryTime = nowQueryTime

    #antlr4 of the codes and conversion from python qiskit to QCSR
    circuitJson = ""
    
    try:
        tree = conversor.generateTree(document["content"], document["language"])
    except Exception as e:
        #print(document["path"])
        #print(f"Se ha producido una excepción: {e}") 
        #print(traceback.print_stack())
        
        error_key = str(e)
        
        if not error_key in errors_dict:
            errors_dict[str(e.args[0])] = [e]
        else:
            errors_dict[str(e.args[0])].append(e)
        
        continue
                
    try:
        circuitJson = conversor.deepSearch(tree, document["language"])
    except Exception as e:
        #print(document["path"])
        #print(f"Se ha producido una excepción: {e}") 
        #print(traceback.print_stack())
        
        error_key = str(e)
        
        if not error_key in errors_dict:
            errors_dict[str(e.args[0])] = [e]
        else:
            errors_dict[str(e.args[0])].append(e)
            
        if str(e.args[0]) == "cannot access local variable 'qubit' where it is not associated with a value":
            print(document["path"])
        
        counterErrorCircuit+=1
        continue
    
    print(circuitJson)
    counterCircuit+=1
    
print(f"Number of generated circuits: {counterCircuit}")
print(f"Number of errors: {counterErrorCircuit}")


# print(errors_dict)


for k in errors_dict:
    print(str(len(errors_dict[k])) + " --> " + str(k))
    

# res = ' \n'.join(sorted(errors_dict, key=lambda key: len(errors_dict[key])))
#
# # Printing result
# print("Sorted keys by value list : " + res)