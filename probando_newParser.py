from src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Parser import Python3Visitor
import ast

file_name = "C:\\Users\\Miriam\\Desktop\\Patrones\\creatingCircuits.py"
#file_name = "C:\\Users\\Miriam\\Desktop\\Patrones\\src\\business\\controller\\Qiskit_QCSR_Conversor\\example\\list_error.py"

with open(file_name, 'r') as file:
    data = file.read()

    astTree = ast.parse(data)
    visitor = Python3Visitor()
    visitor.visit(astTree)
    print(visitor.variables)
    
    for circuit in visitor.circuits.values():
        print(circuit.__str__())