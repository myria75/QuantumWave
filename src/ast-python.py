import ast
import io


# Code
code = "printf(\"asdkfj\");"

code="alakjf af; alksafj dsa,alksaf lksajfldafjkklasaf@@@#@**"

codeFile = "C:/Users/Miriam/Desktop/Patrones/src/business/controller/Qiskit_QCSR_Conversor/example/Python_qiskit_qiskit-community_qiskit-algorithms_qiskit_algorithms.gradients.reverse.derive_circuit.py"
file=open(codeFile,"r")



#code = file.read()

#print(code)

# AST Generation
try:
    tree = ast.parse(code)
    print(ast.dump(tree, indent=3))
except SyntaxError as e:
    print("Hay error: " + str(e))
    #logger.error('Failed to upload to ftp: %s', e)



# Output
#Module(body=[Assign(targets=[Name(id=’qc’, ctx=Store())],value=Call(func=Name(id=’QuantumCircuit’, ctx=Load()),args=[Constant(value=3),Constant(value=3)],keywords=[]))],type_ignores=[])