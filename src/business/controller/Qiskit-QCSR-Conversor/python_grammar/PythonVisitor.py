from antlr4 import *
from antlr4.tree import *
from python_grammar.PythonParser import PythonParser
from python_grammar.PythonParserVisitor import PythonParserVisitor

class PythonVisitor(PythonParserVisitor):

    content = ""
    def __init__(self):
        self.content = ""

    #obtain number of qubits
    def visitName(self, ctx:PythonParser.NameContext):
        if ctx.getText() == "QuantumRegister":
            quantity = ctx.parentCtx.parentCtx
            if isinstance(quantity, PythonParser.ExprContext):
                quantity = int(quantity.getChild(1).getChild(0).getChild(1).getChild(0).getChild(0).getText())
                self.content = [[] for _ in range(quantity)] #create empty qubit array
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#quantum_gates_definition.
    def visitQuantum_gates_definition(self, ctx:PythonParser.Quantum_gates_definitionContext):
        gate = ctx.getRuleContext().getText()
        found_gate = False
        single_qubit_gates = {
            "H": ctx.HADAMARD(),
            "S": ctx.S(),
            "T": ctx.T(),
            "X": ctx.X(),
            "Y": ctx.Y(),
            "Z": ctx.Z(),
            "MEASURE": ctx.MEASURE()
        }
        
        for key,value in single_qubit_gates.items():
            if value is not None: #checks if there's some single qubit gates
                qubit = int(ctx.parentCtx.getChild(2).getChild(1).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                for i in range(0, len(self.content)):
                    if i == qubit:
                        self.content[i].append(key) 
                    else:
                        self.content[i].append("_")

                #print(f"{gate}({qubit})")
                
                found_gate = True
                break
                
        if not found_gate:
            if ctx.CONTROLLEDX() is not None:
                both_qubits = ctx.parentCtx.getChild(2).getChild(1)
                qubit1 = int(both_qubits.getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                qubit2 = int(both_qubits.getChild(2).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                
                for i in range(0, len(self.content)):
                    if i == qubit1:
                        self.content[i].append({"CONTROL":qubit2}) 
                    else:
                        self.content[i].append("_")
                
                #print(f"{gate}({qubit})")
                found_gate = True
        
        return self.visitChildren(ctx) 
