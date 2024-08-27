import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
import ast

#file_name = "C:\\Users\\Miriam\\Desktop\\Patrones\\qubit_error.py"
file_name = "C:\\Users\\Miriam\\Desktop\\Patrones\\test6.py"
#file_name = "C:\\Users\\Miriam\\Desktop\\Patrones\\test2.py"

with open(file_name, 'r') as file:
    data = file.read()

    circuitJson = ""
    astTree = conversor.generateTree(data, "Python")
    #print(ast.dump(astTree, indent=2))

    circuitJson = conversor.visitTree(astTree, "Python")
    print(circuitJson)