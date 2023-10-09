
import json
import os
import webbrowser

from antlr4 import *
from python_grammar.PythonLexer import PythonLexer
from python_grammar.PythonParser import PythonParser
from python_grammar.PythonVisitor import PythonVisitor
from python_grammar.PythonVisitor import PythonParserVisitor

#TODO: CAMBIAR LA MANERA DE IMPORTAR
import sys
sys.path.append('C:\\Users\\Miriam\\Desktop\\Patrones\\src\\business\\controller')
from QmetricsAPI.qmetrics_functions import *

qPainter_url = 'http://172.20.48.7:8000/'


def generateTree(input):
    input_stream = FileStream(input)
    lexer = PythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonParser(stream)
    tree = parser.root()
    return tree

def deepSearch(tree):
    visitor = PythonVisitor()
    visitor.visit(tree)
    #print(visitor.content)
    #TODO: cambiar, manejar error para saltarse circuitos que no devuelvan nada ([] array vacio)
    if len(visitor.content) != 0:
        return json.dumps(visitor.content)
    else:
        return "empty array error"

fileName = "mirilla_example.py"
filePath = os.path.join("example", fileName)
tree = generateTree(os.path.join(os.path.dirname(__file__), filePath))

#"C:\Users\Miriam\Desktop\Patrones\src\business\controller\Qiskit-QCSR-Conversor\example\circuit.py"
circuitJson = deepSearch(tree) #[]

if circuitJson != "empty array error": #TODO: arreglar circuitos que devuelva arrays vacios
    print(circuitJson)
    webbrowser.open(qPainter_url+circuitJson)
    qmetricsjson =  {
        "name" : "MiriamTFGCircuit",
        "circuitCode" : circuitJson
    }
    updateCircuit(qmetricsjson)
    r = calculateMetrics(qmetricsjson)
    metrics = r.json()
    #print(metrics)

    #TODO: PONER BONITO Y BIEN
    from pymongo import MongoClient
    import re

    db_link = 'mongodb://localhost:27017'
    db_name = 'repositories'
    db_coll = 'accepted_code'
    connection = MongoClient(db_link)
    dbGithub = connection[db_name]
    collRepo = dbGithub[db_coll]

    pattern = re.compile(fr".*{re.escape(fileName)}$")
    query = {"path": {"$regex": pattern}}

    results = list(collRepo.find(query))
    print(len(results))
    if len(results) > 0: #comprueba que esta en mongo
        result = results[0]
        result["metrics"]=metrics
        print(result["id"])
        queryBorrado = {"id": result["id"]} #borra la entrada
        collRepo.delete_one(query)

        collRepo.insert_one(result) #inserta la nueva con la metrica
