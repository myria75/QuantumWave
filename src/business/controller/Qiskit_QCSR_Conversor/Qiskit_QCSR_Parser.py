import ast
from builtins import isinstance
from .VariableNotCalculatedException import VariableNotCalculatedException
from .OperationNotFoundException import OperationNotFoundException
from src.business.controller.Qiskit_QCSR_Conversor.Circuit_creation import Circuit_creation

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
    
complex_r_gates = {    
    "crz": "RZ",
    "cry": "RY",
    "crx": "RX"
}

single_r_gate = {
    "rx": "RX",
    "ry": "RY",
    "rz": "RZ"
}

simple_oracle_gate = {
    "u": "ORACLE"
}

simple_gate_all_qubits = {
    "measure_all": "MEASURE"
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
    ast.Pow: "**",
    ast.FloorDiv: "//", 
    ast.BitXor: "^", 
    ast.LShift: "<<",
    ast.RShift: ">>",
    ast.BitOr: "|",
    ast.BitAnd: "&"
}

all_simple_gates = list(single_qubit_gates.keys()) + list(single_r_gate.keys()) + list(simple_oracle_gate.keys()) + list(simple_gate_all_qubits.keys()) #mix all simple gates inside an array
#all_complex_gates = list(complex_qubit_gates.keys()) + list(complex_oracle_gate.keys()) + list(complex_r_gates.keys()) #mix all complex gates inside an array


class Python3Visitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = {} #variable dictionary with values
        self.content = ""
        self.circuits = {}
        
    def storeRegister(self, targetId, argument, regType):
        quantity = 0 # PARA CASOS COMO q = QuantumRegister(2), qiskit.quantumregister, circuit.quantumregister
        
        if isinstance(argument, ast.Constant): #if the argument is a number, takes it
            quantity = int(argument.value)
        elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
            quantity = self.variables[argument.id]
                            
        self.variables[targetId] = regType, quantity
        
    
    def initializeCircuit(self, argument):
        quantity = 0 #quantumcircuit(0), circuit.quantumcircuit(), qiskit.quantumcircuit
                
        if isinstance(argument, int):
            quantity = argument
        if isinstance(argument, ast.Constant): #if the argument is a number, takes it
            quantity = int(argument.value)
        elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
            quantity = self.variables[argument.id] #checks if its in variables dicitonary
            if isinstance(quantity, tuple) and quantity[0] == "QuantumRegister": #checks if its a tuple, when ocurred q=QuantumRegister(2), circuit=QuantumCircuit(q)
                quantity = quantity[1]
        
        self.content = [[] for _ in range(quantity)] #create empty qubit array
    
    def assignRegister(self, idCircuit, nodeArgs):
        if len(nodeArgs) > 0:
            for nodeArg in nodeArgs:
                if isinstance(nodeArg, ast.Name) or isinstance(nodeArg, ast.Constant):
                    argument = self.getNumValue(nodeArg) #comprobar argumentos si es un register
                    if isinstance(argument, tuple) and argument[0] == "QuantumRegister":
                        self.circuits[idCircuit].addRegister(argument[1], nodeArg.id)
                    else:
                        self.circuits[idCircuit].addRegister(argument)                            
                elif isinstance(nodeArg, ast.Call) and nodeArg.func.id == "QuantumRegister":
                    qubits = self.getNumValue(nodeArg.args[0])
                    self.circuits[idCircuit].addRegister(qubits)
        
    
    def translateList(self, nodeList: ast.List) -> list:
        qubits_arrays=[] #circuit.h([1,2,3]) solo se aplica en puertas, guardar variables como arrays
        
        for elt in nodeList.elts:
            qubits_arrays.append(self.getNumValue(elt))
            
        return qubits_arrays
                    
    def getNumValue(self, node):
        try:
            qubit = None
            if isinstance(node, ast.Constant) and isinstance(node, ast.Num): #if the node is a number, takes it
                qubit = int(node.value)
            elif isinstance(node, ast.Name): #if the node is a variable, takes its value from the dictionary
                qubit = self.variables[node.id]
            elif isinstance(node, ast.BinOp): # if its a operation symbol, it executes the operation 
                operator = operations.get(type(node.op))
                if operator is None:
                    raise OperationNotFoundException()

                left = self.getNumValue(node.left) 
                right = self.getNumValue(node.right) 
                
                qubit = eval("{}{}{}".format(left, operator, right))
            
            if qubit is None:
                raise VariableNotCalculatedException()
            else:
                return qubit
                #if isinstance(qubit, tuple): #si se encuentra una tupla al leer de las variables, se queda con el segundo valor quantumregister
                #    return int(qubit[1])
                #else:
                #    return qubit
                
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
                
    def insertSimpleGate(self, circuit_id, gate, node):
        QCSRgate = ''
        qubitArgument = ''
        #if circuit.h(qubit=q[3]) occurs, qubitArgument=q[3]
        #if circuit.h(q[2]) occurs, qubitArgument=q[2]
        keywordQubitExists = False
        needsArguments = True
                
        if len(node.keywords) > 0: #cuando remarca que es qubit= en circuit.h(qubit=q[3])
            for keyword in node.keywords:
                if keyword.arg == "qubit":
                    keywordQubitExists = True
                    if gate in simple_gate_all_qubits:
                        needsArguments = False
                        QCSRgate = simple_gate_all_qubits[gate]    
                    else:
                        qubitArgument = keyword.value # toma el valor del cubit
                        if gate in single_qubit_gates:    
                            QCSRgate = single_qubit_gates[gate]
                        elif gate in single_r_gate:    
                            QCSRgate = single_r_gate[gate] 
                        elif gate in simple_oracle_gate:    
                            QCSRgate = simple_oracle_gate[gate] 
                               
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
            elif gate in simple_gate_all_qubits:
                needsArguments = False
                QCSRgate = simple_gate_all_qubits[gate]    

            
        if not needsArguments:
            for qubit in range(len(self.circuits[circuit_id].registers)):
               self.circuits[circuit_id].insertGate(QCSRgate, qubit) 
        else:
            if isinstance(qubitArgument, ast.Constant) or isinstance(qubitArgument, ast.Name):
                qubit=self.getNumValue(qubitArgument)
                self.circuits[circuit_id].insertGate(QCSRgate, qubit)
            elif isinstance(qubitArgument, ast.Subscript):
                qubit = self.getNumValue(qubitArgument.slice)
                name = qubitArgument.value.id
                self.circuits[circuit_id].insertGate(QCSRgate, qubit, name)
            elif isinstance(qubitArgument, ast.List):
                for elt in qubitArgument.elts:
                    if isinstance(elt, ast.Constant) or isinstance(elt, ast.Name):
                        qubit=self.getNumValue(elt)
                        self.circuits[circuit_id].insertGate(QCSRgate, qubit)
                    elif isinstance(elt, ast.Subscript):
                        qubit = self.getNumValue(elt.slice)
                        name = elt.value.id
                        self.circuits[circuit_id].insertGate(QCSRgate, qubit, name)

            
            #TODO: check list
        
#    def insertComplexGate(self, gate, nodeArgs):
#        QCSRgate = ''
#        qubit_1 = ''
#        qubit_2 = ''
                
#        if gate in complex_qubit_gates:
#            QCSRgate = complex_qubit_gates[gate] 
#            qubit_1 = self.getNumValue(nodeArgs[0])
#            qubit_2 = self.getNumValue(nodeArgs[1]) 
#        elif gate in complex_oracle_gate:
#            QCSRgate = complex_oracle_gate[gate] 
#            qubit_1 = self.getNumValue(nodeArgs[4])
#            qubit_2 = self.getNumValue(nodeArgs[5])
#        elif gate in complex_r_gates:
#            QCSRgate = complex_r_gates[gate] 
#            qubit_1 = self.getNumValue(nodeArgs[1])
#            qubit_2 = self.getNumValue(nodeArgs[2])
            
#        self.fillWithBlanks(qubit_1, qubit_2)
#        self.content[qubit_1].append({"CONTROL":qubit_2})
#        self.content[qubit_2].append(QCSRgate)
            
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                try:
                    if isinstance(node.value, ast.Constant):
                        if str(node.value.value).isnumeric():
                            self.variables[target.id] = int(node.value.value)
                    elif isinstance(node.value, ast.Name) or isinstance(node.value, ast.BinOp):
                        self.variables[target.id] = self.getNumValue(node.value) #adds/update the variable in the dictionary
                    elif isinstance(node.value, ast.List):
                        try:
                            self.variables[target.id] = self.translateList(node.value)
                        except:
                            continue
                    #Store the variable for the register of the circuit
                    elif isinstance(node.value, ast.Call) and hasattr(node.value, 'func'):
                        ##############
                        if isinstance(node.value.func, ast.Name) and node.value.func.id == "QuantumCircuit":
                            id_circuit = target.id#revisar el id                                                          
                            self.circuits[id_circuit] = Circuit_creation(id_circuit)
                            self.assignRegister(id_circuit, node.value.args)
        
                
                        elif isinstance(node.value.func, ast.Name) and (node.value.func.id == "ClassicalRegister" or node.value.func.id == "QuantumRegister"): #q = QuantumRegister(2)
                            self.storeRegister(target.id, node.value.args[0], node.value.func.id)
                        elif hasattr(node.value.func, 'value'):
                            #q = circuit.QuantumRegister(2) || q = qiskit.QuantumRegister(2)
                            if hasattr(node.value.func.value, 'id') and isinstance(node.value.func, ast.Attribute) and (node.value.func.value.id == "circuit" or node.value.func.value.id == "qiskit") and hasattr(node.value.func, 'attr') and (node.value.func.attr == "ClassicalRegister" or node.value.func.attr == "QuantumRegister"):
                                self.storeRegister(target.id, node.value.args[0], node.value.func.attr)
                        
                except VariableNotCalculatedException:
                    self.generic_visit(node) 
        self.generic_visit(node)
        
    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            circuit_id = node.func.value.id
            if node.func.attr == "add_register":
                self.assignRegister(circuit_id, node.args)
            else:
                gate = node.func.attr #door            
                
                #If a simple gate was found
                if gate in all_simple_gates:
                    self.insertSimpleGate(circuit_id, gate, node)
            
    #     #Cuando se crean circuitos con el formato QC=QuantumCircuit(2)
    #     if isinstance(node.func, ast.Name):
    #         if node.func.id == "QuantumCircuit" and len(node.args) > 0: #checks to initialize qubit array
              
    #           self.initializeCircuit(node.args[0])  
    #     elif isinstance(node.func, ast.Attribute):
    #         if hasattr(node.func, 'attr') and node.func.attr == "add_register":
    #             if isinstance(node.args[0], ast.Call) and node.args[0].func.id == "QuantumRegister":
    #                 self.initializeCircuit(self.getNumValue(node.args[0].args[0]))
    #             else:
    #                 qubits = self.getNumValue(node.args[0])
                    
    #                 if isinstance(qubits, tuple) and qubits[0] == "QuantumRegister":
    #                     self.initializeCircuit(qubits[1])
    #                 else:
    #                     self.initializeCircuit(qubits)
    #         #Cuando se crean circuitos con el formato QC=circuit.QuantumCircuit(2) || qiskit.QuantumCircuit
    #         elif hasattr(node.func, 'value') and hasattr(node.func.value, 'id') and (node.func.value.id == "circuit" or node.func.value.id == "qiskit") and hasattr(node.func, 'attr') and node.func.attr == "QuantumCircuit":
    #             if len(node.args) > 0:
    #                 self.initializeCircuit(node.args[0]) #location of the qubit
    
    #         else:
    #             gate = node.func.attr #door            
                
    #             #If a simple gate was found
    #             if gate in all_simple_gates:
    #                 self.insertSimpleGate(gate, node)
            
    #             #Or if a complex gate was found
    #             #elif gate in all_complex_gates:
    #             #    self.insertComplexGate(gate, node.args)
                
        self.generic_visit(node)