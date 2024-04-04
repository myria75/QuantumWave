from src.business.controller.Qiskit_QCSR_Conversor.Circuit_creation import Circuit_creation

circuit = Circuit_creation("prueba")
circuit.addRegister(2, "qr1") #qr1 = QuantumRegister(2)
circuit.addRegister(3, "qr2") #qr2 = QuantumRegister(3)

circuit.insertGate("H", 0)
circuit.insertGate("H", 1, "qr2")


circuit2 = Circuit_creation("prueba")
circuit2.addRegister(2, "qrX") #qr1 = QuantumRegister(2)

circuit2.insertGate("X", 0)

print(circuit.__str__())