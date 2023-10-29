'''Module for finding patterns in a circuit with qiskit simulation'''

from qiskit import QuantumCircuit, execute, Aer

def transpose_nonsquare(matrix):
    '''Returns the transposed SQUARED matrix for squared and non-squared matrices'''
    trans_coords = (max([len(row) for row in matrix]), len(matrix))
    trans = [[0 for _ in range(trans_coords[1])] for _ in range(trans_coords[0])]

    for i in range(trans_coords[0]):
        for j in range(trans_coords[1]):
            try:
                trans[i][j] = matrix[j][i]
            except IndexError:
                trans[i][j] = '_'

    return trans

def symmetry(circuit):
    '''Tries to find a symmetric part of the circuit regarding one/more columns'''
    transposed = transpose_nonsquare(circuit)
    reverse = transposed[::-1]
    return reverse == transposed

def gate_in_entity(gate_qub, gate, entities):
    '''Looks for the control entity index where the gate's qubit is. Oth. returns -1'''
    for i, entity in enumerate(entities):
        if gate_qub in (entity[0] + (entity[1],)) or\
            gate['CONTROL'] in (entity[0] + (entity[1],)):
            return i

    return -1

def get_ctrl_entities(column):
    '''Returns the controlled entities in the given column as a list of lists'''
    entities = []
    for i, gate in enumerate(column):
        if type(gate) == dict and 'CONTROL' in gate.keys():
            entity = gate_in_entity(i, gate, entities)
            if entity == -1:
                new_ctrl = (i,)
                new_tgt = gate['CONTROL']
                entities.append([new_ctrl, new_tgt])
            else:
                prev = entities[entity]
                new_tgt = prev[1]
                if prev[1] == i: # The new control was the target
                    new_tgt = gate['CONTROL']
                entities[entity] = [(i,) + prev[0], new_tgt]

    return entities

def get_permutation_info(entity, n_qubits):
    '''Calculates permutation for reaching entity and extra info'''
    # Calculate string list for entity goal
    goal = []
    for i in range(n_qubits):
        if i in entity[0]: # Ctrl qubit
            goal.append('C')
        elif i == entity[1]: # Tgt qubit
            goal.append('T')
        else:
            goal.append('_')

    # Calculate string list for qiskit control() method
    start = ['C' for _ in range(len(entity[0]))]
    start.append('T')
    start = start + ['_' for _  in range(n_qubits - (len(entity[0]) + 1))]

    # Get permutation indices
    permut_indices = sorted(range(len(goal)), key=goal.__getitem__)
    return permut_indices, goal

def in_entities(ctrl_entities, qubit_no):
    '''Checks whether the given qubit number is in any entity of the list'''
    for entity in ctrl_entities:
        if qubit_no in entity[0] or qubit_no == entity[1]:
            return True
    return False

class Simulator:
    '''
        Class with methods and attributes for receiving,
        translating and simulating a quantum circuit
    '''

    def __init__(self, circuit):
        self.sim_backend = Aer.get_backend('statevector_simulator')
        self.circuit_list = circuit
        self.qc = QuantumCircuit(len(circuit), 1)
        self.statevectors = [0,0]

    def define_circ(self):
        '''Translates the matrix circuit into Qiskit Quantum Circuit'''
        circ_trans = transpose_nonsquare(self.circuit_list) # To work with columns

        for j, col in enumerate(circ_trans):
            # 0) Check if stop and get statevector if so
            # 0.1) First Measurement
            if j == 0:
                self.statevectors[0] = self.get_statevector()

            # 1) Apply controlled entities
            ctrl_entities = get_ctrl_entities(col)
            for entity in ctrl_entities:
                permut_indices, goal_list = get_permutation_info(entity, len(col))
                tmp = QuantumCircuit(1 + goal_list.count('_'))
                self.apply_gate(col[entity[1]], 0, tmp)
                c_gate = tmp.to_gate().control(len(entity[0]))
                self.qc.append(c_gate,permut_indices)


            # 2) Apply normal gates
            for qubit_no, gate in enumerate(col):
                if not in_entities(ctrl_entities, qubit_no):
                    if ':' in gate:
                        rotation_gate, angle_str = gate.split(':')
                        if rotation_gate in {'RX','RY','RZ'}:
                            self.apply_gate((rotation_gate, float(angle_str)), qubit_no, self.qc)
                    self.apply_gate(gate, qubit_no, self.qc)

            # 0.2) Second Measurement
            if len(circ_trans) - 1:
                self.statevectors[1] = self.get_statevector()

    def apply_gate(self, gate, qubit, qc):
        '''Applies the given gate to qiskit quantum circuit qc'''
        if type(gate) == dict and 'SWAP' in gate.keys():
            qc.swap(qubit, gate['SWAP'])
        else:
            if gate == 'I':
                qc.id(qubit)
            elif gate == 'X' or gate == 'RX':
                qc.x(qubit)
            elif gate == 'Y' or gate == 'RY':
                qc.y(qubit)
            elif gate == 'Z' or gate == 'RZ':
                qc.z(qubit)
            elif gate == 'H':
                qc.h(qubit)
            elif gate == 'S':
                qc.s(qubit)
            elif gate == 'SR':
                qc.sdg(qubit)
            elif gate == 'T':
                qc.t(qubit)
            elif gate == 'TR':
                qc.tdg(qubit)
            elif gate == 'MEASURE':
                qc.measure(qubit, 0)
            elif gate == 'R1':
                qc.x(qubit)
            elif gate == '_':
                pass
            else:
                pass

    def get_statevector(self):
        '''Returns the statevector of the circuit currently'''
        job = execute(self.qc, backend=self.sim_backend)
        result = job.result()
        return result.get_statevector(self.qc)

    def state_condition(self):
        '''True if both statevectors are the same, False oth.'''
        return True if self.statevectors[0] == self.statevectors[1] else False

def main(circuit, verbose=False, qasm=False):
    '''Checks if uncompute pattern is in the given circuit. 1 if match, 2 if partial, 0 otherwise'''
    if len(circuit) == 1 and len(circuit[0]) == 0:
        return 0
    is_symmetric = symmetry(circuit)
    if is_symmetric: # Is symmetric?
        sim = Simulator(circuit)
        sim.define_circ()
        if verbose:
            print('## CIRCUIT INFO ##')
            print(sim.qc.draw('text'))
            print(sim.statevectors)
        if qasm:
            print('## QASM CIRCUIT TRANSLATION ##')
            print(sim.qc.qasm())

        if sim.state_condition(): # Same statevector?
            return 1
        else: # Symmetric but not equivalent
            return 2
    return 0

if __name__ == '__main__':
    if main(
        [
            ["X",{"ORACLE":2},"RX",{"SWAP":1},"RX",{"ORACLE":2},"MEASURE"],
            ["Y","ORACLE2","RY","SWAP2","RY","ORACLE2","MEASURE"]
        ],
        verbose=True,
        qasm=True
    ):
        print('Uncompute pattern found!!!!')
    else:
        print('Uncompute pattern not found :(')
