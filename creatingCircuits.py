from qiskit.circuit import QuantumRegister, QuantumCircuit

q = QuantumRegister(2)
circuit1 = QuantumCircuit(q)
circuit1.h(1)
# [], [H]

q2 = QuantumRegister(3)
circuit2 = QuantumCircuit(q2)
circuit2.h(q2[0])
# [H], [], []

circuit3 = QuantumCircuit(QuantumRegister(3))
circuit3.h(2)
# [], [], [H]

circuit4 = QuantumCircuit()
circuit4.add_register(QuantumRegister(1))
circuit4.h(0)
# [H]

c5_q1 = QuantumRegister(2)
c5_q2 = QuantumRegister(3)
circuit5 = QuantumCircuit(c5_q1, c5_q2)
circuit5.h(1)
# [], [H], [], [], []

c6_q1 = QuantumRegister(2)
c6_q2 = QuantumRegister(3)
circuit6 = QuantumCircuit(c6_q1, c6_q2)
circuit6.h(c6_q2[0])
# [], [], [H], [], []


circuit7 = QuantumCircuit(QuantumRegister(3), QuantumRegister(2))
circuit7.h(1)
# [], [H], [], [], []


circuit8 = QuantumCircuit()
c8_qr1 = QuantumRegister(2)
c8_qr2 = QuantumRegister(3)
c8_qr3 = QuantumRegister(4)
circuit8.add_register(c8_qr1)
circuit8.add_register(c8_qr2, c8_qr3)
circuit8.h(c8_qr1[0])
circuit8.x(c8_qr2[1])
# [H], [], [], [X], [], [], [], [], []

circuit9 = QuantumCircuit(2)
c9_qr = QuantumRegister(3)
circuit9.add_register(c9_qr, QuantumRegister(1))
circuit9.x(c9_qr[0])
# [], [], [X], [], [], []

circuit10 = QuantumCircuit(5)
circuit10.x([0, 1, 2])
# [X], [X], [X], [], []

c11_qr = QuantumRegister(4)
circuit11 = QuantumCircuit(c11_qr)
circuit11.x([0, c11_qr[1]])
circuit11.measure_all()
# [X, MEASURE], [X, MEASURE], [MEASURE], [MEASURE], [MEASURE]

circuit12 = QuantumCircuit(2)
circuit12.x(qubit=0)
# [X], []

c13_qr = QuantumRegister(3)
circuit13 = QuantumCircuit(c13_qr)
circuit13.x(qubit=c13_qr[0])
# [X], [], []

circuit14 = QuantumCircuit(2)
circuit14.x(qubit=[0,1])
# [X], [X]

circuit15 = QuantumCircuit(2)
circuit15.cx(0,1)
# [CONTROL:1], [X]

circuit16 = QuantumCircuit(2)
circuit16.cx(control_qubit=0, target_qubit=1)
# [CONTROL:1], [X]