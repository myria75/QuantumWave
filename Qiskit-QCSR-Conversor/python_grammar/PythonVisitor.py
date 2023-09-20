from antlr4 import *
from antlr4.tree import *
from python_grammar.PythonParser import PythonParser
from python_grammar.PythonParserVisitor import PythonParserVisitor
import json 

class PythonVisitor(PythonParserVisitor):

    content = ""
    def __init__(self):
        self.content = ""

    # Visit a parse tree produced by PythonParser#quantum_gates_definition.
    def visitQuantum_gates_definition(self, ctx:PythonParser.Quantum_gates_definitionContext):
        gate = ctx.getRuleContext().getText()

        single_qubit_gates = (ctx.HADAMARD(), ctx.S(), ctx.T(), ctx.X(), ctx.Y(), ctx.Z())
        
        if any(item is not None for item in single_qubit_gates): #checks if there's some single qubit gates
            qubit = int(ctx.parentCtx.getChild(2).getChild(1).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
            print(f"{gate}({qubit})")
        elif ctx.CONTROLLEDX() is not None:
            both_qubits = ctx.parentCtx.getChild(2).getChild(1)
            qubit1 = int(both_qubits.getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
            qubit2 = int(both_qubits.getChild(2).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
            print(f"{gate}({qubit1},{qubit2})")
        elif ctx.MEASURE() is not None:
            qubit = int(ctx.parentCtx.getChild(2).getChild(1).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
            print(f"{gate}({qubit})")
            
        
        #importante no perder este regturn
        return self.visitChildren(ctx)