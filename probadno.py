import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor

with open("C:\\Users\\Miriam\\Desktop\\Python_qiskit_qiskit-community_qiskit-algorithms_test.test_phase_estimator.py", "r") as file:
    content = file.read()
    antlr_tree = conversor.generateTree(content, "Python")
    circuitJson = conversor.deepSearch(antlr_tree, "Python")