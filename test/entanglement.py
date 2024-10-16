from src.business.controller.Qiskit_QCSR_Conversor.detectEntanglement import detectEntanglement

# converted_circuits = {
#     "noentanglement": [[{"CONTROL":2},{"CONTROL":3},{"CONTROL":4}],[],["X"],["_","X"],["_","_","X"]],
#     "sientanglement": [["H",{"CONTROL":1}],["_","X"]],
#     "sientanglement": [["H",{"CONTROL":1},"Y"],["_","X","Z"]], 
#     "prueba": [["X","_","_","_","Y"],["Y","H","_","_","_",{"CONTROL":4}],["_","_","Z"],["Z","X","_","X"],["_","_","_","_","_","X"]],
#     "prueba2":[["X","_","_","Y"],["Y","H",{"CONTROL":3},"Z"],[],["Z","_","X"]]
# }

print(detectEntanglement([["X","_","_","_","Y"],["Y","H","_","_","_",{"CONTROL":4}],["_","_","Z"],["Z","X","_","X"],["_","_","_","_","_","X"]]))
