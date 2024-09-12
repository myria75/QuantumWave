from src.business.controller.Qiskit_QCSR_Conversor.detectEntanglement import detectEntanglement
import ast
from builtins import isinstance
from src.business.controller.Qiskit_QCSR_Conversor.VariableNotCalculatedException import VariableNotCalculatedException
from src.business.controller.Qiskit_QCSR_Conversor.OperationNotFoundException import OperationNotFoundException
from src.business.controller.Qiskit_QCSR_Conversor.Circuit_creation import Circuit_creation
from _ast import If

converted_circuits = {
    "noentanglement": [[{"CONTROL":2},{"CONTROL":3},{"CONTROL":4}],[],["X"],["_","X"],["_","_","X"]],
    "sientanglement": [["H",{"CONTROL":1}],["_","X"]],
    "pregunto": [["H",{"CONTROL":1},"Y"],["_","X","Z"]]
}
print(detectEntanglement(converted_circuits))
