
from antlr4 import *
from antlr4.tree import *
if "." in __name__:
    from .qasm3Parser import qasm3Parser
    from .qasm3ParserVisitor import qasm3ParserVisitor
else:
    from qasm3Parser import qasm3Parser
    from qasm3ParserVisitor import qasm3ParserVisitor

class qasm3Visitor(qasm3ParserVisitor):

    content = ""
    single_qubit_gates = {
            "h": "H",
            "s": "S",
            "t": "T",
            "x": "X",
            "y": "Y",
            "z": "Z"
    }
    
    r_oracle_qubit_gates = {
        "rx": "RX",
        "ry": "RY",
        "rz": "RZ",
        "u": {"ORACLE":1}
    }

    complex_qubit_gates = {
        "ch": "H",
        "cy": "Y",
        "cz": "Z"
    }

    r_oracle_complex_qubit_gates = {
        "crx": "RX",
        "cry": "RY",
        "crz": "RZ",
        "cu": {"ORACLE":1}
    }

    def __init__(self):
        self.content = ""

    #para obtener el n de qubits
    def visitOldStyleDeclarationStatement(self, ctx:qasm3Parser.OldStyleDeclarationStatementContext):
        #obtener el primer hijo, comprobar si es QREG
        if ctx.getChild(0).getText() == 'qreg': 
            quantity = int(ctx.getChild(2).getChild(1).getChild(0).getText())
            self.content = [[] for _ in range(quantity)] #create empty qubit array
        
        return self.visitChildren(ctx)
    
    def visitGateCallStatement(self, ctx:qasm3Parser.GateCallStatementContext):
        #hacer un diccionario por cada tipo distinto de puerta (si es de varios qbits, si tiene otros valores, etc)
        gate = ctx.getChild(0).getText()

        if gate in self.single_qubit_gates:
            qubit = int(ctx.getChild(1).getChild(0).getChild(0).getChild(1).getChild(1).getChild(0).getText()) 
            self.content[qubit].append(self.single_qubit_gates[gate])
        elif gate in self.r_oracle_qubit_gates:
            qubit = int(ctx.getChild(4).getChild(0).getChild(0).getChild(1).getChild(1).getChild(0).getText()) 
            self.content[qubit].append(self.r_oracle_qubit_gates[gate])
        elif gate in self.complex_qubit_gates:
            qubit1 = int(ctx.getChild(1).getChild(0).getChild(0).getChild(1).getChild(1).getChild(0).getText()) 
            qubit2 = int(ctx.getChild(1).getChild(2).getChild(0).getChild(1).getChild(1).getChild(0).getText())
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
            self.content[qubit2].append(self.complex_qubit_gates[gate])
        elif gate in self.r_oracle_complex_qubit_gates:   
            qubit1 = int(ctx.getChild(4).getChild(0).getChild(0).getChild(1).getChild(1).getChild(0).getText()) 
            qubit2 = int(ctx.getChild(4).getChild(2).getChild(0).getChild(1).getChild(1).getChild(0).getText())
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
            self.content[qubit2].append(self.r_oracle_complex_qubit_gates[gate])
        #dependiendo de lo que sea, habrá que buscar un hijo u otro
        return self.visitChildren(ctx)
    
    def visitMeasureExpression(self, ctx:qasm3Parser.MeasureExpressionContext):
        qubit = int(ctx.getChild(1).getChild(0).getChild(1).getChild(1).getChild(0).getText()) 
        self.content[qubit].append("MEASURE")
        
        return self.visitChildren(ctx)