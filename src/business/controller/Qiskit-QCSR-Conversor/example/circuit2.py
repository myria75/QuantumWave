from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.cx(qreg_q[0], qreg_q[2])
circuit.h(qreg_q[3])
circuit.h(qreg_q[0])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.measure(qreg_q[3], creg_c[3])
circuit.t(qreg_q[0])
circuit.z(qreg_q[1])