import ast
import io

# Code
code = "System.out.println();"

#codeFile = "C:/Users/Miriam/Desktop/Patrones/src/business/controller/Qiskit_QCSR_Conversor/example/Python_qiskit_qiskit-community_qiskit-algorithms_qiskit_algorithms.amplitude_estimators.ae.py"
#file=open(codeFile,"r")

#code = file.read()

#print(code)

# AST Generation
print(ast.dump(ast.parse(code), indent=3))

# Output
#Module(body=[Assign(targets=[Name(id=’qc’, ctx=Store())],value=Call(func=Name(id=’QuantumCircuit’, ctx=Load()),args=[Constant(value=3),Constant(value=3)],keywords=[]))],type_ignores=[])