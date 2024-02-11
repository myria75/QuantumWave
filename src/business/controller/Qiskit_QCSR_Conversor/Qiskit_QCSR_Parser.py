import ast
from builtins import isinstance
from .VariableNotCalculatedException import VariableNotCalculatedException

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

operations = {
    ast.Add: "+",
    ast.Sub: "-",
    ast.Mult: "*",
    ast.Div: "/",
    ast.Mod: "%"
}

all_simple_gates = list(single_qubit_gates.keys()) + list(single_r_gate.keys()) + list(simple_oracle_gate.keys())

class Python3Visitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = {} #variable dictionary with values
        self.content = ""
        
    def getNumValue(self, node):
        try:
            if isinstance(node, ast.Constant) and isinstance(node, ast.Num): #if the node is a number, takes it
                qubit = int(node.value)
            elif isinstance(node, ast.Name): #if the node is a variable, takes its value from the dictionary
                qubit = self.variables[node.id]
            elif isinstance(node, ast.BinOp):
                left = self.getNumValue(node.left)
                right = self.getNumValue(node.right)
                operator = operations.get(type(node.op))
                if operator is None:
                    print("error, opracion no encontrada ")
        
                qubit = eval("{}{}{}".format(left, operator, right))
            elif isinstance(node, ast.Subscript):
                qubit = self.getNumValue(node.slice)
            return int(qubit)
        except (ValueError, KeyError):
            raise VariableNotCalculatedException()
    
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
            if isinstance(target, ast.Name):
                try:
                    if isinstance(node.value, ast.Constant):
                        if str(node.value.value).isnumeric():
                            self.variables[target.id] = int(node.value.value)
                    elif isinstance(node.value, ast.Name) or isinstance(node.value, ast.BinOp):
                        self.variables[target.id] = self.getNumValue(node.value) #adds/update the variable in the dictionary
                    #almacena la variable para el registro del circuito
                    elif isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "QuantumRegister":
                        self.variables[target.id] = 'QuantumRegister'
                except VariableNotCalculatedException:
                    self.generic_visit(node) 
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
            
            #If a simple gate was found
            if gate in all_simple_gates:
                QCSRgate = ''
                argument = ''
                    
                if gate in single_qubit_gates:    
                    QCSRgate = single_qubit_gates[gate]
                    argument = node.args[0]
                elif gate in single_r_gate:    
                    QCSRgate = single_r_gate[gate] 
                    argument = node.args[1]
                elif gate in simple_oracle_gate:    
                    QCSRgate = simple_oracle_gate[gate] 
                    argument = node.args[3]
                
                #Comprueba si se le ha pasado un QuantumRegister
                if isinstance(argument, ast.Name) and argument.id in self.variables and self.variables[argument.id] == 'QuantumRegister':
                    for qubit_index in range(0, len(self.content)): 
                        self.content[qubit_index].append(QCSRgate)
                #O una variable/número
                else:
                    qubit = self.getNumValue(argument)
                    self.content[qubit].append(QCSRgate)
        
        
            if gate in complex_qubit_gates:    
                QCSRgate = complex_qubit_gates[gate] 
                qubit_1 = self.getNumValue(node.args[0])
                qubit_2 = self.getNumValue(node.args[1])
                self.fillWithBlanks(qubit_1, qubit_2)
                self.content[qubit_1].append({"CONTROL":qubit_2})
                self.content[qubit_2].append(QCSRgate)
                

            
            if gate in complex_oracle_gate:    
                QCSRgate = complex_oracle_gate[gate] 
                qubit_1 = self.getNumValue(node.args[4])
                qubit_2 = self.getNumValue(node.args[5])
                self.fillWithBlanks(qubit_1, qubit_2)
                self.content[qubit_1].append({"CONTROL":qubit_2})
                self.content[qubit_2].append(QCSRgate)
            
        self.generic_visit(node)

#codigoParseado: ast.Module = ast.parse(code)
#visitor = Python3Visitor()
#visitor.visit(codigoParseado)
#print(visitor.variables)
#print(visitor.content)