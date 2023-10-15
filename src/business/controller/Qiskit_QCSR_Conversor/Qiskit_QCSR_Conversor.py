
import json
import os
import webbrowser

from antlr4 import *
from src.business.controller.Qiskit_QCSR_Conversor.python_grammar.PythonLexer import PythonLexer
from src.business.controller.Qiskit_QCSR_Conversor.python_grammar.PythonParser import PythonParser
from src.business.controller.Qiskit_QCSR_Conversor.python_grammar.PythonVisitor import PythonVisitor
from src.business.controller.Qiskit_QCSR_Conversor.python_grammar.PythonVisitor import PythonParserVisitor

#TODO: CAMBIAR LA MANERA DE IMPORTAR
import sys
sys.path.append('C:\\Users\\Miriam\\Desktop\\Patrones\\src\\business\\controller')
#from QmetricsAPI.qmetrics_functions import *

qPainter_url = 'http://172.20.48.7:8000/'

def generateTree(input):
    input_stream = InputStream(input)
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