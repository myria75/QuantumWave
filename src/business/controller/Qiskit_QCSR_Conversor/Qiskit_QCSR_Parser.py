import ast
from builtins import isinstance
from .VariableNotCalculatedException import VariableNotCalculatedException

# dictionaries with all kind of gates
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
    ast.Mod: "%",
    ast.Pow: "**"
}

circuits = { }

all_simple_gates = list(single_qubit_gates.keys()) + list(single_r_gate.keys()) + list(simple_oracle_gate.keys()) #mix all simple gates inside an array
all_complex_gates = list(complex_qubit_gates.keys()) + list(complex_oracle_gate.keys()) #mix all complex gates inside an array


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
            elif isinstance(node, ast.BinOp): # if its a operation symbol, it executes the operation 
                left = self.getNumValue(node.left) 
                right = self.getNumValue(node.right) 
                operator = operations.get(type(node.op))
                
                if operator is None:
                    print("ERROR: Not found operation")
        
                qubit = eval("{}{}{}".format(left, operator, right))
            elif isinstance(node, ast.Subscript): #some of the operations are from a type of operation
                qubit = self.getNumValue(node.slice)
            if isinstance(qubit, tuple): #si se encuentra una tupla al leer de las variables, y s eueda con el segundo valor 
                return int(qubit[1])
            else:
                return int(qubit)
        except (ValueError, KeyError):
            raise VariableNotCalculatedException()
        
    def fillWithBlanks(self, q1, q2): #Function to draw the QCSR circuit with blank spaces if its needed
        index = 0
        
        if len(self.content[q1]) > len(self.content[q2]):
            index = len(self.content[q1])         
            while len(self.content[q2]) != index:
                self.content[q2].append("_")
        else:
            index = len(self.content[q2])
            while len(self.content[q1]) != index:
                self.content[q1].append("_")
                
    def insertSimpleGate(self, gate, node):
        QCSRgate = ''
        qubitArgument = ''
        #if circuit.h(qubit=q[3]) occurs, qubitArgument=q[3]
        #if circuit.h(q[2]) occurs, qubitArgument=q[2]
 
        keywordQubitExists = False
                
        if len(node.keywords) > 0: #cuando remarca que es qubit= en circuit.h(qubit=q[3])
            for keyword in node.keywords:
                if keyword.arg == "qubit":
                    keywordQubitExists = True
                            
                    if gate in single_qubit_gates:    
                        QCSRgate = single_qubit_gates[gate]
                    elif gate in single_r_gate:    
                        QCSRgate = single_r_gate[gate] 
                    elif gate in simple_oracle_gate:    
                        QCSRgate = simple_oracle_gate[gate] 
                               
                    qubitArgument = keyword.value # toma el valor del cubit
                            
        if not keywordQubitExists:                                      
            #It depends on the type of the door, it gets traduced to QCSR and obtains from the argument where it should be appended
            if gate in single_qubit_gates:    
                QCSRgate = single_qubit_gates[gate]
                qubitArgument = node.args[0]
            elif gate in single_r_gate:    
                QCSRgate = single_r_gate[gate] 
                qubitArgument = node.args[1]
            elif gate in simple_oracle_gate:    
                QCSRgate = simple_oracle_gate[gate] 
                qubitArgument = node.args[3]
                            
        #ÉSTE CASO: circuit.h(q)
        #Check if the argument its a QuantumRegister
        if isinstance(qubitArgument, ast.Name) and qubitArgument.id in self.variables and self.variables[qubitArgument.id][0] == 'QuantumRegister':
            for qubit_index in range(0, len(self.content)): 
                self.content[qubit_index].append(QCSRgate)
        #Or is a variable or a number
        else:
            qubit = self.getNumValue(qubitArgument)
            self.content[qubit].append(QCSRgate)
        
    def insertComplexGate(self, gate, nodeArgs):
        QCSRgate = ''
        qubit_1 = ''
        qubit_2 = ''
                
        if gate in complex_qubit_gates:
            QCSRgate = complex_qubit_gates[gate] 
            qubit_1 = self.getNumValue(nodeArgs[0])
            qubit_2 = self.getNumValue(nodeArgs[1]) 
        elif gate in complex_oracle_gate:
            QCSRgate = complex_oracle_gate[gate] 
            qubit_1 = self.getNumValue(nodeArgs[4])
            qubit_2 = self.getNumValue(nodeArgs[5])
            
        self.fillWithBlanks(qubit_1, qubit_2)
        self.content[qubit_1].append({"CONTROL":qubit_2})
        self.content[qubit_2].append(QCSRgate)
            
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                try:
                    if isinstance(node.value, ast.Constant):
                        if str(node.value.value).isnumeric():
                            self.variables[target.id] = int(node.value.value)
                    elif isinstance(node.value, ast.Name) or isinstance(node.value, ast.BinOp):
                        self.variables[target.id] = self.getNumValue(node.value) #adds/update the variable in the dictionary
                    #Store the variable for the register of the circuit
                    elif isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "QuantumRegister":
                        quantity = 0 # PARA CASOS COMO q = QuantumRegister(2)
                        argument = node.value.args[0]
                        if isinstance(argument, ast.Constant): #if the argument is a number, takes it
                            quantity = int(argument.value)
                        elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
                            quantity = self.variables[argument.id]
                        
                        self.variables[target.id] = 'QuantumRegister', quantity #stores value of qubits in dictionary
                except VariableNotCalculatedException:
                    self.generic_visit(node) 
        self.generic_visit(node)
        
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "QuantumCircuit": #checks to initialize qubit array
                quantity = 0
                argument = node.args[0] #location of the qubit
                
                if isinstance(argument, ast.Constant): #if the argument is a number, takes it
                    quantity = int(argument.value)
                elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
                    quantity = self.variables[argument.id] #checks if its in variables dicitonary
                    if isinstance(quantity, tuple): #checks if its a tuple
                        quantity = quantity[1]
                self.content = [[] for _ in range(quantity)] #create empty qubit array
    
        elif isinstance(node.func, ast.Attribute):
            gate = node.func.attr #door            
            
            #If a simple gate was found
            if gate in all_simple_gates:
                self.insertSimpleGate(gate, node)
        
            #Or if a complex gate was found
            elif gate in all_complex_gates:
                self.insertComplexGate(gate, node.args)
                
        self.generic_visit(node)
