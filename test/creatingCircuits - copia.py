from qiskit.circuit import QuantumRegister, QuantumCircuit

q = QuantumRegister(2)
circuit1 = QuantumCircuit(q)
circuit1.h(1)
circuit1.cx(0, 1)