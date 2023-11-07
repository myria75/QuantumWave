from antlr4 import *
from antlr4.tree import *
if "." in __name__:
    from .PythonParser import PythonParser
    from .PythonParserVisitor import PythonParserVisitor
else:
    from PythonParser import PythonParser
    from PythonParserVisitor import PythonParserVisitor

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
                self.content[qubit].append(key)

                #print(f"{gate}({qubit})")
                
                found_gate = True
                break
            
        if not found_gate:
            complex_qubit_gates = {
                "H": ctx.CONTROLLEDH(),
                "X": ctx.CONTROLLEDX(),
                "Z": ctx.CONTROLLEDZ()
            }
            
            for key,value in complex_qubit_gates.items():
                if value is not None:
                    both_qubits = ctx.parentCtx.getChild(2).getChild(1)
                    qubit1 = int(both_qubits.getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                    qubit2 = int(both_qubits.getChild(2).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                    index = 0

                    if len(self.content[qubit1]) > len(self.content[qubit2]):
                        index = len(self.content[qubit1])
                        
                        while len(self.content[qubit2]) != index:
                            self.content[qubit2].append("_")
                    else:
                        index = len(self.content[qubit2])
                        
                        while len(self.content[qubit1]) != index:
                            self.content[qubit1].append("_")

                    self.content[qubit1].append({"CONTROL":qubit2})
                    self.content[qubit2].append(key)
                    
                    #print(f"{gate}({qubit})")
                    found_gate = True
                    break
        
        if not found_gate:
            simple_oracle_gate = {
                "ORACLE": ctx.ORACLE()
            }
            
            for key,value in simple_oracle_gate.items():
                if value is not None: #checks if there's some single qubit gates
                    qubit = int(ctx.parentCtx.getChild(2).getChild(1).getChild(6).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                    self.content[qubit].append({key:1})
                    found_gate = True
                    break
        
        if not found_gate:
            complex_oracle_gate = {
                "ORACLE": ctx.CONTROLLEDU()
            }
            for key,value in complex_oracle_gate.items():
                if value is not None:
                    both_qubits = ctx.parentCtx.getChild(2).getChild(1)
                    qubit1 = int(both_qubits.getChild(8).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                    qubit2 = int(both_qubits.getChild(10).getChild(0).getChild(0).getChild(0).getChild(0).getChild(1).getChild(0).getChild(1).getText())
                    index = 0
                    if len(self.content[qubit1]) > len(self.content[qubit2]):
                        index = len(self.content[qubit1])
                        
                        while len(self.content[qubit2]) != index:
                            self.content[qubit2].append("_")
                    else:
                        index = len(self.content[qubit2])
                        
                        while len(self.content[qubit1]) != index:
                            self.content[qubit1].append("_")

                    self.content[qubit1].append({"CONTROL":qubit2})
                    self.content[qubit2].append({key:1})
                    found_gate = True
                    break

        return self.visitChildren(ctx) 