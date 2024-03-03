class Circuit_creation():
    name:str = ""
    registers = {}
    lastCustomReg = 0

    def __init__(self, name=""):
        self.name = name
        self.registers = {}
        self.lastCustomReg = 0
    
    def addRegister(self, length, name="_"):
        for i in range(0, length):
            id = ""
            if name!="_": 
                id = f"{name}_{i}"
            else:
                id = f"_{i+1+self.lastCustomReg}"
                
            self.registers[id] = []
        if name=="_":
            self.lastCustomReg = self.lastCustomReg + length
        
    def insertGate(self, gate, qubit, name="_"):
        #TODO: throw exception if name doesn't exist
        if name!="_":
            id = f"{name}_{qubit}"
        else:
            regsKeyList = list(self.registers.keys())
            id = regsKeyList[qubit]
        self.registers[id].append(gate)
    
    def convertToQCSR(self):
        result=[]
        
        for values in self.registers.values():
            result.append(values)
        
        return result
    
    def __str__(self):
        return f'''
        Name: {self.name},
        Registers: {self.registers.__str__()},
        Circuit: {self.convertToQCSR()}'''