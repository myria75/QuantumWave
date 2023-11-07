from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.u(pi / 2, pi / 2, pi / 2, qreg_q[2])
circuit.cu(pi / 2, pi / 2, pi / 2, 0, qreg_q[0], qreg_q[2])