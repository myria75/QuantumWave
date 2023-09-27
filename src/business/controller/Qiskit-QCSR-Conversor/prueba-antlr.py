
from antlr4 import *
from python_grammar.PythonLexer import PythonLexer
from python_grammar.PythonParser import PythonParser
from python_grammar.PythonVisitor import PythonVisitor
from python_grammar.PythonVisitor import PythonParserVisitor
from ..QmetricsAPI.qmetrics_functions import *
import os
import json

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

filePath = os.path.join("example", "circuit.py")
tree = generateTree(os.path.join(os.path.dirname(__file__), filePath))

#"C:\Users\Miriam\Desktop\Patrones\src\business\controller\Qiskit-QCSR-Conversor\example\circuit.py"

circuitJson = deepSearch(tree)

print(calculateMetrics(circuitJson))
