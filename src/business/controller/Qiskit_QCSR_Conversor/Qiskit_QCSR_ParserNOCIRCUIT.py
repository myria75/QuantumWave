import ast
from builtins import isinstance
from .VariableNotCalculatedException import VariableNotCalculatedException
from .OperationNotFoundException import OperationNotFoundException

circuits = { }

class Python3Visitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = {} #variable dictionary with values
        self.content = ""
        self.contadorQuantumRegister = 0
        self.contadorQuantumCircuit = 0
        
    def storeRegister(self, targetId, argument, regType):
        if regType == "QuantumRegister":
            self.contadorQuantumRegister+=1

        # quantity = 0 # PARA CASOS COMO q = QuantumRegister(2), qiskit.quantumregister, circuit.quantumregister
        
        # if isinstance(argument, ast.Constant): #if the argument is a number, takes it
        #     quantity = int(argument.value)
        # elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
        #     quantity = self.variables[argument.id]
                            
        # self.variables[targetId] = regType, quantity
        
    
    def initializeCircuit(self, argument):
        self.contadorQuantumCircuit+=1
        # quantity = 0 #quantumcircuit(0), circuit.quantumcircuit(), qiskit.quantumcircuit
                
        # if isinstance(argument, int):
        #     quantity = argument
        # if isinstance(argument, ast.Constant): #if the argument is a number, takes it
        #     quantity = int(argument.value)
        # elif isinstance(argument, ast.Name): #if the argument is a variable, takes its value from the dictionary
        #     quantity = self.variables[argument.id] #checks if its in variables dicitonary
        #     if isinstance(quantity, tuple) and quantity[0] == "QuantumRegister": #checks if its a tuple, when ocurred q=QuantumRegister(2), circuit=QuantumCircuit(q)
        #         quantity = quantity[1]
        
        # self.content = [[] for _ in range(quantity)] #create empty qubit array


            
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):     
                #Store the variable for the register of the circuit
                if isinstance(node.value, ast.Call) and hasattr(node.value, 'func'):
                    if isinstance(node.value.func, ast.Name) and (node.value.func.id == "ClassicalRegister" or node.value.func.id == "QuantumRegister"): #q = QuantumRegister(2)
                        self.storeRegister(target.id, node.value.args[0], node.value.func.id)
                    elif hasattr(node.value.func, 'value'):
                        #q = circuit.QuantumRegister(2) || q = qiskit.QuantumRegister(2)
                        if hasattr(node.value.func.value, 'id') and isinstance(node.value.func, ast.Attribute) and (node.value.func.value.id == "circuit" or node.value.func.value.id == "qiskit") and hasattr(node.value.func, 'attr') and (node.value.func.attr == "ClassicalRegister" or node.value.func.attr == "QuantumRegister"):
                            self.storeRegister(target.id, node.value.args[0], node.value.func.attr)
                        

        self.generic_visit(node)
        
    def visit_Call(self, node):
        #Cuando se crean circuitos con el formato QC=QuantumCircuit(2)
        if isinstance(node.func, ast.Name):
            if node.func.id == "QuantumCircuit" and len(node.args) > 0: #checks to initialize qubit array
              
              self.initializeCircuit(node.args[0])  
        elif isinstance(node.func, ast.Attribute):
            if hasattr(node.func, 'attr') and node.func.attr == "add_register":
                if isinstance(node.args[0], ast.Call) and node.args[0].func.id == "QuantumRegister":
                    self.initializeCircuit()
                else:
                    qubits = 0
                    
                    if isinstance(qubits, tuple) and qubits[0] == "QuantumRegister":
                        self.initializeCircuit(qubits[1])
                    else:
                        self.initializeCircuit(qubits)
            #Cuando se crean circuitos con el formato QC=circuit.QuantumCircuit(2) || qiskit.QuantumCircuit
            elif hasattr(node.func, 'value') and hasattr(node.func.value, 'id') and (node.func.value.id == "circuit" or node.func.value.id == "qiskit") and hasattr(node.func, 'attr') and node.func.attr == "QuantumCircuit":
                if len(node.args) > 0:
                    self.initializeCircuit(node.args[0]) #location of the qubit
    
        self.generic_visit(node)