from src.business.controller.Qiskit_QCSR_Conversor.detectEntanglement import detectEntanglement
import ast
from builtins import isinstance
from src.business.controller.Qiskit_QCSR_Conversor.VariableNotCalculatedException import VariableNotCalculatedException
from src.business.controller.Qiskit_QCSR_Conversor.OperationNotFoundException import OperationNotFoundException
from src.business.controller.Qiskit_QCSR_Conversor.Circuit_creation import Circuit_creation
from _ast import If

converted_circuits = {
    "qc": [[{"CONTROL":2},{"CONTROL":3},{"CONTROL":4}],[],["X"],["_","X"],["_","_","X"]],
    "qc": [[{"CONTROL":4}],["_",{"CONTROL":4}],["_","_",{"CONTROL":4}],[],["X","X","X"]],
    "qc": [[{"CONTROL":1}], ["X"], ["H"], []],
}

print(detectEntanglement(converted_circuits))

{
    "c1": True,
    
}