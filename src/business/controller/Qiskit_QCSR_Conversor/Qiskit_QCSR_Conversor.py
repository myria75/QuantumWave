
"""Generate antlr4 tree, and conversion from qiskit and openqasm to QCSR
"""

import json
from .EmptyCircuitException import EmptyCircuitException
from antlr4 import *
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.PythonLexer import PythonLexer
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.PythonParser import PythonParser
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.PythonVisitor import PythonVisitor
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Lexer import qasm3Lexer
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Parser import qasm3Parser
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Visitor import qasm3Visitor

def generateTree(input, language):
    input_stream = InputStream(input)
    tree = ''

    if language == 'Python':
        lexer = PythonLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PythonParser(stream)
        tree = parser.root()
    elif language == 'openqasm':
        lexer = qasm3Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = qasm3Parser(stream)
        tree = parser.program()

    return tree

def deepSearch(tree, language):
    visitor = ''

    if language == 'Python':
        visitor = PythonVisitor()
    elif language == 'openqasm':
        visitor = qasm3Visitor()

    visitor.visit(tree) #The circuit array is stored in visitor.content 
    
    if len(visitor.content) == 0:
        raise EmptyCircuitException()
    
    return json.dumps(visitor.content)