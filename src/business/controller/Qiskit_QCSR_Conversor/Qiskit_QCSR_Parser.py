import ast

single_qubit_gates = {
    "h": "H",
    "s": "S",
    "t": "T",
    "x": "X",
    "y": "Y",
    "z": "Z",
    "measure": "MEASURE"
}

complex_qubit_gates = {
    "ch": "H",
    "cx": "X",
    "cz": "Z"
}

single_r_gate = {
    "rx": "RX",
    "ry": "RY",
    "rz": "RZ"
}

simple_oracle_gate = {
    "u": "ORACLE"
}

complex_oracle_gate = {
    "cu": "ORACLE"
}

class VariableVisitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = {} #varible dictionary with values
        self.content = ""
        
    def getNumValue(self, node):
        if isinstance(node, ast.Constant): #if the node is a number, takes it
            qubit = int(node.value)
        elif isinstance(node, ast.Name): #if the node is a variable, takes its value from the dictionary
            qubit = self.variables[node.id]
        return int(qubit)
    
    def fillWithBlanks(self, q1, q2):
        index = 0

        if len(self.content[q1]) > len(self.content[q2]):
            index = len(self.content[q1])         
            while len(self.content[q2]) != index:
                self.content[q2].append("_")
        else:
            index = len(self.content[q2])
            while len(self.content[q1]) != index:
                self.content[q1].append("_")

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and isinstance(node.value, ast.Num):
                self.variables[target.id] = node.value.n #adds/update the variable in the dictionary
        self.generic_visit(node)
        
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "QuantumRegister": #checks to initialize qubit array
                quantity = 0
                argument = node.args[0]
                if isinstance(argument, ast.Constant): #if the argument is a number, takes it
                    quantity = int(argument.value)
                elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
                    quantity = self.variables[argument.id]
                
                self.content = [[] for _ in range(quantity)] #create empty qubit array
                
        if isinstance(node.func, ast.Attribute):
            gate = node.func.attr #door
            
            if gate in single_qubit_gates:    
                QCSRgate = single_qubit_gates[gate] 
                qubit = self.getNumValue(node.args[0].slice)
                self.content[qubit].append(QCSRgate)
        
            if gate in complex_qubit_gates:    
                QCSRgate = complex_qubit_gates[gate] 
                qubit_1 = self.getNumValue(node.args[0].slice)
                qubit_2 = self.getNumValue(node.args[1].slice)
                self.fillWithBlanks(qubit_1, qubit_2)
                self.content[qubit_1].append({"CONTROL":qubit_2})
                self.content[qubit_2].append(QCSRgate)
                
            if gate in single_r_gate:    
                QCSRgate = single_r_gate[gate] 
                qubit = self.getNumValue(node.args[1].slice)
                self.content[qubit].append(QCSRgate)
        
            if gate in simple_oracle_gate:    
                QCSRgate = simple_oracle_gate[gate] 
                qubit = self.getNumValue(node.args[3].slice)
                self.content[qubit].append(QCSRgate)
            
            if gate in complex_oracle_gate:    
                QCSRgate = complex_oracle_gate[gate] 
                qubit_1 = self.getNumValue(node.args[4].slice)
                qubit_2 = self.getNumValue(node.args[5].slice)
                self.fillWithBlanks(qubit_1, qubit_2)
                self.content[qubit_1].append({"CONTROL":qubit_2})
                self.content[qubit_2].append(QCSRgate)
                    
        self.generic_visit(node)
    
code = '''
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.cu(pi / 2, pi / 2, pi / 2, 0, qreg_q[0], qreg_q[2])
'''

#print(ast.dump(ast.parse(code), indent=2))
codigoParseado: ast.Module = ast.parse(code)
visitor = VariableVisitor()
visitor.visit(codigoParseado)
#print(visitor.variables)
print(visitor.content)