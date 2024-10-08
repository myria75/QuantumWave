
"""Circuit object that is introduced into QCSR format, manage with registers and its names
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

class Circuit_creation():
    name:str = ""
    registers = {}
    lastCustomReg = 0 #registers with no id assigned 

    def __init__(self, name=""):
        self.name = name
        self.registers = {}
        self.lastCustomReg = 0
    
    def addRegister(self, length, name="_"): #len to indicate the quantity of registers that we must put 
        for i in range(0, length):
            id = ""
            if name!="_": 
                id = f"{name}_{i}"
            else:
                id = f"_{i+1+self.lastCustomReg}"
                
            self.registers[id] = []
        if name=="_":
            self.lastCustomReg = self.lastCustomReg + length
        
    def insertGate(self, gate, qubit="_", name="_"):
        #TODO: throw exception if name doesn't exist
        if not(qubit is None) and not(qubit=="_"):
            if name!="_": #circuit.h(qr[0]) -> insertGate("H", 0, "qr")
                id = f"{name}_{qubit}"
            else: #circuit.h(0) -> insertGate("H", 0)
                regsKeyList = list(self.registers.keys())
                id = regsKeyList[qubit]
            self.registers[id].append(gate)
        else:
            for id in self.registers: # takes the name, goes throw dict to search if the name starts by _, and if its true, append 
                if id.startswith(f"{name}_"):
                    self.registers[id].append(gate)
        
    def insertControl(self, controlled_qubit, insert_qubit, controlled_name="_", insert_name="_"):
        regsKeyList = list(self.registers.keys())
        nameId_controlled_qubit = ""
        if controlled_name!="_": 
            nameId_controlled_qubit = f"{controlled_name}_{controlled_qubit}"
        else: 
            nameId_controlled_qubit = regsKeyList[controlled_qubit]
        
        position = regsKeyList.index(nameId_controlled_qubit)
        self.insertGate({"CONTROL":position}, insert_qubit, insert_name)
    
    def convertToQCSR(self):
        result=[]
        
        for values in self.registers.values():
            result.append(values)
        
        for sub_array in result:
            while sub_array and sub_array[-1] == '_':
                sub_array.pop()
        
        return result
    
    def fillWithBlanks(self, qubit1, qubit2, name1="_", name2="_"): #Function to draw the QCSR circuit with blank spaces if its needed
        index = 0
        control_qubit = 0
        target_qubit = 0
        
        if name1!="_": #cases like: circuit.h(qr[0]) -> insertGate("H", 0, "qr")
            control_qubit = f"{name1}_{qubit1}"
        else: #cases like: circuit.h(0) -> insertGate("H", 0)
            regsKeyList = list(self.registers.keys())
            control_qubit = regsKeyList[qubit1]
            
        if name2!="_": #cases like: circuit.h(qr[0]) -> insertGate("H", 0, "qr")
            target_qubit = f"{name2}_{qubit2}"
        else: #cases like: circuit.h(0) -> insertGate("H", 0)
            regsKeyList = list(self.registers.keys())
            target_qubit = regsKeyList[qubit2]
        
        if len(self.registers[control_qubit]) > len(self.registers[target_qubit]):
            index = len(self.registers[control_qubit])         
            while len(self.registers[target_qubit]) != index:
                self.registers[target_qubit].append("_")
        else:
            index = len(self.registers[target_qubit])
            while len(self.registers[control_qubit]) != index:
                self.registers[control_qubit].append("_")
                
    def fillOthersWithBlanks(self, qubit1, qubit2, name1="_", name2="_"):
        control_qubit = 0
        target_qubit = 0
        
        if name1!="_": #cases like: circuit.h(qr[0]) -> insertGate("H", 0, "qr")
            control_qubit = f"{name1}_{qubit1}"
        else: #cases like: circuit.h(0) -> insertGate("H", 0)
            regsKeyList = list(self.registers.keys())
            control_qubit = regsKeyList[qubit1]
            
        if name2!="_": #cases like: circuit.h(qr[0]) -> insertGate("H", 0, "qr")
            target_qubit = f"{name2}_{qubit2}"
        else: #cases like: circuit.h(0) -> insertGate("H", 0)
            regsKeyList = list(self.registers.keys())
            target_qubit = regsKeyList[qubit2]
        
        for qubit_id in self.registers:
            if control_qubit!=qubit_id and target_qubit!=qubit_id:
                self.registers[qubit_id].append("_")
            
    def __str__(self):
        return f'''
        Name: {self.name},
        Registers: {self.registers.__str__()},
        Circuit: {self.convertToQCSR()}'''