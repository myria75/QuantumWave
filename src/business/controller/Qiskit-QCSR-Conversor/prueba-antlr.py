
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
#from QmetricsAPI.qmetrics_functions import *

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
    return json.dumps(visitor.content)

filePath = os.path.join("example", "circuit2.py")
tree = generateTree(os.path.join(os.path.dirname(__file__), filePath))

#"C:\Users\Miriam\Desktop\Patrones\src\business\controller\Qiskit-QCSR-Conversor\example\circuit.py"
circuitJson = deepSearch(tree)
print(circuitJson)
webbrowser.open(qPainter_url+circuitJson)
#print(calculateMetrics(circuitJson))
