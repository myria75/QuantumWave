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
        
        if isinstance(node.func, ast.Attribute):
            gate = node.func.attr #door
            
            if gate in single_qubit_gates:    
                QCSRgate = single_qubit_gates[gate] 
                qubit = self.getNumValue(node.args[0].slice)
                self.content[qubit].append(QCSRgate)
        
                
        self.generic_visit(node)
    
code = '''
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.cx(qreg_q[0], qreg_q[1])
'''

print(ast.dump(ast.parse(code), indent=2))
#codigoParseado: ast.Module = ast.parse(code)
#visitor = VariableVisitor()
#visitor.visit(codigoParseado)
#print(visitor.variables)
#print(visitor.content)