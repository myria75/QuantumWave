
"""Counts how many quantum registers and quantum circuits are in one file from the dataset
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

import ast
import configparser
import time
from src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_ParserNOCIRCUIT import Python3Visitor as PythonVisitorNOCIRCUIT
from src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Parser2 import Python3Visitor as PythonVisitorWITHCIRCUIT
from src.business.controller.Qiskit_QCSR_Conversor.EmptyCircuitException import EmptyCircuitException
import os

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

counterParsedFile = 0
counterCircuit = 0

counterManyRegistersNOCIRC = 0
counterManyCircuitsNOCIRC = 0

counterManyRegistersWITHCIRC = 0
counterManyCircuitsWITHCIRC = 0

for document in documents:
    nowQueryTime = time.time()
    if nowQueryTime - startQueryTime >= refreshTime:
        documents.close()
        documents = collRepo.find(query, no_cursor_timeout=True)
        startQueryTime = nowQueryTime

    #ast of the codes and conversion from python qiskit to QCSR
    circuitJson = ""
    
    try:
        tree = ast.parse(document["content"])
    except Exception as e:        
        continue

    counterParsedFile+=1

    #count without converting to circuit
    try:
        visitor1 = PythonVisitorNOCIRCUIT()
        visitor1.visit(tree)

        if visitor1.contadorQuantumRegister > 1:
            counterManyRegistersNOCIRC+=1
        
        if visitor1.contadorQuantumCircuit > 1:
            counterManyCircuitsNOCIRC+=1

    except Exception as e:
        pass
    
    #count with converting to circuit
    try:
        visitor2 = PythonVisitorWITHCIRCUIT()
        visitor2.visit(tree)

        if len(visitor2.content) == 0:
            raise EmptyCircuitException()
        blank_qubits = 0
        for qubit in visitor2.content:
            if len(qubit) == 0:
                blank_qubits+=1
        if blank_qubits == len(visitor2.content):
            raise EmptyCircuitException()
    
        if visitor2.contadorQuantumRegister > 1:
            counterManyRegistersWITHCIRC+=1
        
        if visitor2.contadorQuantumCircuit > 1:
            counterManyCircuitsWITHCIRC+=1

        counterCircuit+=1

    except Exception as e:
        pass
    
print(f"Number of parsed files: {counterParsedFile}")
print(f"Number of parsed files with generated circuit: {counterCircuit}")
print(f"Number of files with >1 registers: {counterManyRegistersNOCIRC} ({round((counterManyRegistersNOCIRC/counterParsedFile)*100, 2)} % of parsed files)")
print(f"Number of files with >1 registers: {counterManyRegistersWITHCIRC} ({round((counterManyRegistersWITHCIRC/counterCircuit)*100, 2)} % of circuits)")
print(f"Number of files with >1 circuits: {counterManyCircuitsNOCIRC} ({round((counterManyCircuitsNOCIRC/counterParsedFile)*100, 2)} % of parsed files)")
print(f"Number of files with >1 circuits: {counterManyCircuitsWITHCIRC} ({round((counterManyCircuitsWITHCIRC/counterCircuit)*100, 2)} % of circuits)")