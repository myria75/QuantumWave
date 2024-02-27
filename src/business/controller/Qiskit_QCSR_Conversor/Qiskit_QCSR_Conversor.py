
"""Generate antlr4 tree, and conversion from qiskit and openqasm to QCSR
"""

import json
import ast
from .EmptyCircuitException import EmptyCircuitException
from antlr4 import *
from src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Parser import Python3Visitor
#from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.Python3Lexer import Python3Lexer as PythonLexer
#from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.Python3Parser import Python3Parser as PythonParser
#from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.Python3Visitor import Python3Visitor as PythonVisitor
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Lexer import qasm3Lexer
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Parser import qasm3Parser
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Visitor import qasm3Visitor

def generateTree(input, language):
    input_stream = InputStream(input)
    tree = ''

    if language == "Python":
        tree = ast.parse(input)
        
        #Old lexer:
        #lexer = PythonLexer(input_stream)
        #stream = CommonTokenStream(lexer)
        #parser = PythonParser(stream)
        #tree = parser.root()
        ##tree = parser.file_input()
        
    elif language == "openqasm":
        lexer = qasm3Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = qasm3Parser(stream)
        tree = parser.program()

    return tree


def generateTreeAndPrint(input, language):
    tree = generateTree(input, language)
    print(ast.dump(tree, indent=2))

def visitTree(tree, language):
    visitor = None

    if language == "Python":
        visitor = Python3Visitor()
        #visitor = PythonVisitor()
    elif language == "openqasm":
        visitor = qasm3Visitor()

    visitor.visit(tree) #The circuit array is stored in visitor.content 
    
    if len(visitor.content) == 0:
        raise EmptyCircuitException()

    blank_qubits = 0

    for qubit in visitor.content:
        if len(qubit) == 0:
            blank_qubits+=1
    
    if blank_qubits == len(visitor.content):
        raise EmptyCircuitException()
    
    return json.dumps(visitor.content)

