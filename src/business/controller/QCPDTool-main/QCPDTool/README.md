# Pattern List Definition
The patterns that QCPDTool looks for are:
- [Oracle](https://quantumcomputingpatterns.org/#/patterns/19): Found if and only if:
    1. An oracle gate is correctly placed.
- [Initialization](https://quantumcomputingpatterns.org/#/patterns/15): Found under the following conditions:
    1. Only Pauli gates are used.
    2. The gates are placed before any Hadamard, rotation or oracle gate.
    3. The gates cannot be used as target in a control gate.
- [Superposition](https://quantumcomputingpatterns.org/#/patterns/16): Found if fulfilled:
    1. Only the Hadamard gate is used.
    2. The gates are applied simultaneously.
- [Entanglement](https://quantumcomputingpatterns.org/#/patterns/17): Found under the next conditions:
    1. A **Superposition** is placed in $N-M$ (where $N$ is the number of qubits involved in the entanglement; and $M$ the number of target qubits).
    2. (Multi or Single) CNOT gate must use as control qubits those $N-M$.
    3. The previous CNOT gate must use as target qubit the remaining $M$ qubits.
- [Uncompute](https://quantumcomputingpatterns.org/#/patterns/20). Found if and only if:
    1. There exists a symmetry regarding a middle set of gates.
    2. The final state after the gate's batch is the same as the initial one.