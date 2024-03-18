
"""Generate ast tree, and conversion from qiskit and openqasm to QCSR
"""

import json
import ast
from .EmptyCircuitException import EmptyCircuitException
from antlr4 import *
from src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Parser import Python3Visitor
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Lexer import qasm3Lexer
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Parser import qasm3Parser
from src.business.controller.Qiskit_QCSR_Conversor.languages_grammar.qasm3Visitor import qasm3Visitor

def generateTree(input, language):
    input_stream = InputStream(input)
    tree = ''

    if language == "Python":
        tree = ast.parse(input)
        
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
    
    circuits = {}

    if language == "Python":
        visitor = Python3Visitor()
        visitor.visit(tree)
        circuits = visitor.getConvertedCircuits()
    elif language == "openqasm":
        visitor = qasm3Visitor()
        visitor.visit(tree)
        if len(visitor.content) == 0:
            raise EmptyCircuitException()
        circuits["_1"] = visitor.content

    
    #filter empty circuits
    dict_circuits = circuits.copy()
    
    for key, circuit in dict_circuits.items():
        if circuit == [] or circuit is None: #removes empty circuits
            del circuits[key]
        else:
            #checks for circuits like [[], [], [], []]
            blank_qubits = 0

            for qubit in circuit:
                if len(qubit) == 0:
                    blank_qubits+=1
            
            if blank_qubits == len(circuit):
                del circuits[key]
            else:
                #converts circuits to string
                circuits[key] = json.dumps(circuit)
            
    if len(circuits) == 0:
        raise EmptyCircuitException()
    
    return circuits