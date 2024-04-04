from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from sys import argv

a1 = QuantumRegister(1)
a1c = ClassicalRegister(1)
a0 = QuantumRegister(1)
a0c = ClassicalRegister(1)
b1 = QuantumRegister(1)
b1c = ClassicalRegister(1)
b0 = QuantumRegister(1)
b0c = ClassicalRegister(1)

c0 = QuantumRegister(1)
c0c = ClassicalRegister(1)

t0 = QuantumRegister(1)
t0c = ClassicalRegister(1)

c1 = QuantumRegister(1)
c1c = ClassicalRegister(1)

c2 = QuantumRegister(1)
c2c = ClassicalRegister(1)

t1 = QuantumRegister(1)
t1c = ClassicalRegister(1)

c3 = QuantumRegister(1)
c3c = ClassicalRegister(1)

#beginning of the circuit
circuit = QuantumCircuit(a1,a0,b1,b0,c3,c2,c1,c0,t0,t1,a1c,a0c,b1c,b0c,c3c,c2c,c1c,c0c,t0c,t1c)

circuit.ccx(a0[0],b1[0],t0[0])
circuit.ccx(a0[0],b0[0],c0[0])
circuit.ccx(a1[0],b1[0],t1[0])
circuit.ccx(a1[0],b0[0],c1[0])
circuit.ccx(t0[0],c1[0],c2[0])
circuit.cx(t0[0],c1[0])
circuit.ccx(t1[0],c2[0],c3[0])
circuit.cx(t1[0],c2[0])

#uncompute temporary qubits
circuit.ccx(a1[0],b1[0],t1[0])
circuit.ccx(a0[0],b1[0],t0[0])

circuit.measure(c0,c0c)
circuit.measure(c1,c1c)
circuit.measure(c2,c2c)
circuit.measure(c3,c3c)

execute(circuit)
