
"""Parser that transform from Python-Qiskit language program to QCSR format
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

import ast
from builtins import isinstance
from .VariableNotCalculatedException import VariableNotCalculatedException
from .OperationNotFoundException import OperationNotFoundException
from src.business.controller.Qiskit_QCSR_Conversor.Circuit_creation import Circuit_creation
from _ast import If

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

double_complex_qubit_gates = {
    "ccx": "X",
    "ccz": "Z"
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
    "u":  {"ORACLE": 1}
}

simple_gate_all_qubits = {
    "measure_all": "MEASURE"
}

complex_oracle_gate = {
    "cu": {"ORACLE": 1}
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
all_complex_gates = list(complex_qubit_gates.keys()) + list(complex_oracle_gate.keys()) + list(complex_r_gates.keys()) #mix all complex gates inside an array
all_double_complex_gates = list(double_complex_qubit_gates.keys())

class Python3Visitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = {} #variable dictionary with values
        self.content = ""
        self.circuits = {}
        
    def storeRegister(self, targetId, argument, regType):
        quantity = 0 # cases like: q = QuantumRegister(2), qiskit.quantumregister, circuit.quantumregister
        
        if isinstance(argument, ast.Constant): #if the argument is a number, takes it
            quantity = int(argument.value)
        elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
            quantity = self.variables[argument.id]
                            
        self.variables[targetId] = regType, quantity
        
    def initializeCircuit(self, argument):
        quantity = 0 #cases like: quantumcircuit(0), circuit.quantumcircuit(), qiskit.quantumcircuit
                
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
                    argument = self.getNumValue(nodeArg) #chech arguments if these are registers
                    if isinstance(argument, tuple) and argument[0] == "QuantumRegister":
                        self.circuits[idCircuit].addRegister(argument[1], nodeArg.id)
                    else:
                        if not isinstance(argument, tuple):
                            self.circuits[idCircuit].addRegister(argument)                            
                elif isinstance(nodeArg, ast.Call) and nodeArg.func.id == "QuantumRegister":
                    qubits = self.getNumValue(nodeArg.args[0])
                    self.circuits[idCircuit].addRegister(qubits)
        
    def translateList(self, nodeList: ast.List) -> list:
        qubits_arrays=[] #store variables as an array, gates will be applied on many qubits ex: circuit.h([1,2,3])
        
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
                
        except (ValueError, KeyError):
            raise VariableNotCalculatedException()
        
    def insertSimpleGate(self, circuit_id, gate, node):
        QCSRgate = ''
        qubitArgument = ''
        #if circuit.h(qubit=q[3]) occurs, qubitArgument=q[3]
        #if circuit.h(q[2]) occurs, qubitArgument=q[2]
        keywordQubitExists = False
        needsArguments = True
                
        if len(node.keywords) > 0: #when qubit is clarified qubit= in circuit.h(qubit=q[3])
            for keyword in node.keywords:
                if keyword.arg == "qubit":
                    keywordQubitExists = True
                    if gate in simple_gate_all_qubits:
                        needsArguments = False
                        QCSRgate = simple_gate_all_qubits[gate]    
                    else:
                        qubitArgument = keyword.value # takes the value of the qubit
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
                if isinstance(qubit, tuple):
                    if qubit[0] == "QuantumRegister":
                        name = qubitArgument.id
                        self.circuits[circuit_id].insertGate(QCSRgate, name=name)
                else:
                    self.circuits[circuit_id].insertGate(QCSRgate, qubit)
            elif isinstance(qubitArgument, ast.Subscript):
                qubit = self.getNumValue(qubitArgument.slice)
                name = qubitArgument.value.id
                self.circuits[circuit_id].insertGate(QCSRgate, qubit, name)
            elif isinstance(qubitArgument, ast.List): # if content of the qubit's value its a list
                for elt in qubitArgument.elts:
                    if isinstance(elt, ast.Constant) or isinstance(elt, ast.Name):
                        qubit=self.getNumValue(elt)
                        self.circuits[circuit_id].insertGate(QCSRgate, qubit)
                    elif isinstance(elt, ast.Subscript):
                        qubit = self.getNumValue(elt.slice)
                        name = elt.value.id
                        self.circuits[circuit_id].insertGate(QCSRgate, qubit, name)
            #TODO: check list
        
    def insertComplexGate(self, circuit_id, gate, node):
        QCSRgate = ''
        qubit1Argument = ''
        qubit2Argument = ''
        keywordQubitExists = False
        
        if len(node.keywords) > 0: # as keyword in simple gate, there are keywords specified in control gates like control_gate or target_gate
            for keyword in node.keywords:
                if keyword.arg == "control_qubit": # starts from qubit that controls
                    qubit1Argument = keyword.value
                if keyword.arg == "target_qubit": # ends with qubit that is controlled
                    qubit2Argument = keyword.value
            if qubit1Argument != "" and qubit2Argument != "": # no qubit especified, applies to all qubits
                if gate in complex_qubit_gates:
                    QCSRgate = complex_qubit_gates[gate]
                elif gate in complex_oracle_gate:
                    QCSRgate = complex_oracle_gate[gate]
                elif gate in complex_r_gates:
                    QCSRgate = complex_r_gates[gate]
                keywordQubitExists = True
                
        if not keywordQubitExists: # if keyword doesn't exists, it act as in simple gates
            if gate in complex_qubit_gates:
                QCSRgate = complex_qubit_gates[gate] 
                qubit1Argument = node.args[0]
                qubit2Argument = node.args[1] 
            elif gate in complex_oracle_gate:
                QCSRgate = complex_oracle_gate[gate] 
                qubit1Argument = node.args[4]
                qubit2Argument = node.args[5]
            elif gate in complex_r_gates:
                QCSRgate = complex_r_gates[gate] 
                qubit1Argument = node.args[1]
                qubit2Argument = node.args[2]

        qubit_1 = ''
        name_1 = "_" #default name  
        
        if isinstance(qubit1Argument, ast.Constant) or isinstance(qubit1Argument, ast.Name):
            qubit_1=self.getNumValue(qubit1Argument)
        elif isinstance(qubit1Argument, ast.Subscript):
            qubit_1 = self.getNumValue(qubit1Argument.slice)
            name_1 = qubit1Argument.value.id
        
        qubit_2 = ''
        name_2 = "_"
        
        if isinstance(qubit2Argument, ast.Constant) or isinstance(qubit2Argument, ast.Name):
            qubit_2=self.getNumValue(qubit2Argument)
        elif isinstance(qubit2Argument, ast.Subscript):
            qubit_2 = self.getNumValue(qubit2Argument.slice)
            name_2 = qubit2Argument.value.id

        self.circuits[circuit_id].fillWithBlanks(qubit_1, qubit_2, name_1, name_2)
        self.circuits[circuit_id].insertControl(qubit_2, qubit_1, name_2, name_1)
        self.circuits[circuit_id].insertGate(QCSRgate, qubit_2, name_2)
        self.circuits[circuit_id].fillOthersWithBlanks(qubit_1, qubit_2, name_1, name_2)
        
    def insertDoubleComplexGates(self, circuit_id, gate, node):      
        QCSRgate = ''
        cqubit1Argument = ''
        cqubit2Argument = ''
        qubitArgument = ''
        keywordQubitExists = False
        
        if len(node.keywords) > 0: 
            for keyword in node.keywords:
                if keyword.arg == "control_qubit1": # starts from qubit that controls
                    cqubit1Argument = keyword.value
                if keyword.arg == "control_qubit2": # starts from qubit that controls
                    cqubit2Argument = keyword.value
                if keyword.arg == "target_qubit": # ends with qubit that is controlled
                    qubitArgument = keyword.value
            if cqubit1Argument != "" and cqubit2Argument != "" and qubitArgument != "": # no qubit especified, applies to all qubits
                if gate in complex_qubit_gates:
                    QCSRgate = double_complex_qubit_gates[gate]
                keywordQubitExists = True
                
        if not keywordQubitExists: # if keyword doesn't exists, it act as in simple gates
            if gate in double_complex_qubit_gates:
                QCSRgate = double_complex_qubit_gates[gate] 
                cqubit1Argument = node.args[0]
                cqubit2Argument = node.args[1] 
                qubitArgument = node.args[2]
                
        cqubit_1 = ''
        cname_1 = "_" #default name  
        
        if isinstance(cqubit1Argument, ast.Constant) or isinstance(cqubit1Argument, ast.Name):
            cqubit_1=self.getNumValue(cqubit1Argument)
        elif isinstance(cqubit1Argument, ast.Subscript):
            cqubit_1 = self.getNumValue(cqubit1Argument.slice)
            cname_1 = cqubit1Argument.value.id
        
        cqubit_2 = ''
        cname_2 = "_"
        
        if isinstance(cqubit2Argument, ast.Constant) or isinstance(cqubit2Argument, ast.Name):
            cqubit_2=self.getNumValue(cqubit2Argument)
        elif isinstance(cqubit2Argument, ast.Subscript):
            cqubit_2 = self.getNumValue(cqubit2Argument.slice)
            cname_2 = cqubit2Argument.value.id
            
        tqubit = ''
        tname = "_" #default name  
        
        if isinstance(qubitArgument, ast.Constant) or isinstance(qubitArgument, ast.Name):
            tqubit=self.getNumValue(qubitArgument)
        elif isinstance(qubitArgument, ast.Subscript):
            tqubit = self.getNumValue(qubitArgument.slice)
            tname = qubitArgument.value.id
            
        for i in range(0,2):
            self.circuits[circuit_id].fillWithBlanks(cqubit_1, cqubit_2, cname_1, cname_2)
            self.circuits[circuit_id].fillWithBlanks(cqubit_1, tqubit, cname_1, tname)
            self.circuits[circuit_id].fillWithBlanks(cqubit_2, tqubit, cname_2, tname)
        
        self.circuits[circuit_id].insertControl(cqubit_2, cqubit_1, cname_2, cname_1)
        self.circuits[circuit_id].insertControl(tqubit, cqubit_2, tname, cname_2)
        self.circuits[circuit_id].insertGate(QCSRgate, tqubit, tname) 
        
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
                        if isinstance(node.value.func, ast.Name) and node.value.func.id == "QuantumCircuit":
                            id_circuit = target.id #checks the id                                                        
                            self.circuits[id_circuit] = Circuit_creation(id_circuit)
                            self.assignRegister(id_circuit, node.value.args)
        
                
                        elif isinstance(node.value.func, ast.Name) and (node.value.func.id == "ClassicalRegister" or node.value.func.id == "QuantumRegister"): #q = QuantumRegister(2)
                            self.storeRegister(target.id, node.value.args[0], node.value.func.id)
                        elif hasattr(node.value.func, 'value'):
                            #cases like: q = circuit.QuantumRegister(2) || q = qiskit.QuantumRegister(2)
                            if hasattr(node.value.func.value, 'id') and isinstance(node.value.func, ast.Attribute) and (node.value.func.value.id == "circuit" or node.value.func.value.id == "qiskit") and hasattr(node.value.func, 'attr') and (node.value.func.attr == "ClassicalRegister" or node.value.func.attr == "QuantumRegister"):
                                self.storeRegister(target.id, node.value.args[0], node.value.func.attr)
                        
                except VariableNotCalculatedException:
                    self.generic_visit(node) 
        self.generic_visit(node)
        
    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and hasattr(node.func.value, "id"):
            circuit_id = node.func.value.id
            if node.func.attr == "add_register": #throws when functions add_register are given
                self.assignRegister(circuit_id, node.args)
            else:
                gate = node.func.attr #door            
                
                #If a simple gate was found
                if gate in all_simple_gates:
                    self.insertSimpleGate(circuit_id, gate, node)
                elif gate in all_complex_gates:
                    self.insertComplexGate(circuit_id, gate, node)
                elif gate in all_double_complex_gates:
                    self.insertDoubleComplexGates(circuit_id, gate, node)
            
        self.generic_visit(node)
        
    def getConvertedCircuits(self)->dict:   # obstains the result of the QCSR conversion
        converted_circuits = {}
        for circuit_id, circuit_object in self.circuits.items():
           converted_circuits[circuit_id] = circuit_object.convertToQCSR()     
        return converted_circuits