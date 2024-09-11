
"""Counts number of trees that can be generated from dataset
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

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
counterAst = 0
counterError = 0 

for document in documents:
    nowQueryTime = time.time()
    
    if nowQueryTime - startQueryTime >= refreshTime:
        documents.close()
        documents = collRepo.find(query, no_cursor_timeout=True)
        startQueryTime = nowQueryTime

    #ast of the codes and conversion from python qiskit to QCSR
    circuitJson = ""
    
    try:
        tree = conversor.generateTree(document["content"], document["language"])
    except Exception as e:
        print(document["path"])
        print(f"Se ha producido una excepción: {e}") 
        counterError+=1
        continue
               
    counterAst+=1
    
print(f"Number of generated AST: {counterAst}")
print(f"Number of errors: {counterError}")