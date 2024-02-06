import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor

file_name = "C:\\Users\\Miriam\\Desktop\\Patrones\\qft_7dec.qasm"

with open(file_name, 'r') as file:
    data = file.read()

    circuitJson = ""
    antlr_tree = conversor.generateTree(data, "openqasm")

    circuitJson = conversor.deepSearch(antlr_tree, "openqasm")
    print(circuitJson)