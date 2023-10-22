
"""Generate antlr4 tree, and conversion from qiskit to QCSR
"""

import json
from .EmptyCircuitException import EmptyCircuitException
from antlr4 import *
from src.business.controller.Qiskit_QCSR_Conversor.python_grammar.PythonLexer import PythonLexer
from src.business.controller.Qiskit_QCSR_Conversor.python_grammar.PythonParser import PythonParser
from src.business.controller.Qiskit_QCSR_Conversor.python_grammar.PythonVisitor import PythonVisitor

def generateTree(input):
    input_stream = InputStream(input)
    lexer = PythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonParser(stream)
    tree = parser.root()
    return tree

def deepSearch(tree):
    visitor = PythonVisitor()
    visitor.visit(tree) #The circuit array is stored in visitor.content 
    
    if len(visitor.content) == 0:
        raise EmptyCircuitException()
    
    return json.dumps(visitor.content)