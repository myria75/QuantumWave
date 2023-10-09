'''Implementation for the PatternFinder and the necessary methods for it'''

# Each single-pattern finding method will return a Dictionary, such that each entry has:
#   <id_in_class>: (<qubit_no>, <column_no>, <circuit_fragment>)
# Where:
#   - <id_in_class>: Id for the found pattern within each pattern class.
#   - <qubit_no>: Number of qubit where the pattern starts.
#   - <column_no>: Number of column where the pattern starts.
#   - <circuit_fragment>: QPainter JSON representation of the pattern.

import json
import copy
import multiprocessing

def get_oracle(row, col, circuit):
    '''Extracting the code for the fragment of the circuit with the pattern'''
    fragment = [[{"ORACLE": 1}]]
    height = 0
    for current in circuit[row + 1:]:
        if current[col] != "ORACLE2":
            break
        height += 1
        fragment.append(["ORACLE2"])

    fragment[0][0]["ORACLE"] += height
    return fragment

def is_target(gate_row, column):
    '''Checking whether the simple gate given as input is used as target'''
    for col_gate in column:
        if type(col_gate) == dict:
            if 'CONTROL' in col_gate.keys():
                if col_gate['CONTROL'] == gate_row:
                    return True

    return False

def initialize(coords):
    '''Returns empty matrix with the coords (rows, cols)'''
    matrix = []

    for _ in range(coords[0]):
        row = []
        for _ in range(coords[1]):
            row.append('_')
        matrix.append(row)

    return matrix

def transpose_nonsquare(matrix):
    '''Returns the transposed SQUARED matrix for squared and non-squared matrices.'''
    trans_coords = (max([len(row) for row in matrix]), len(matrix))
    trans = [[0 for _ in range(trans_coords[1])] for _ in range(trans_coords[0])]

    for i in range(trans_coords[0]):
        for j in range(trans_coords[1]):
            try:
                trans[i][j] = matrix[j][i]
            except IndexError:
                trans[i][j] = '_'

    return trans

def fill_hadamards(sup_case):
    '''Returns a fragment with the H gates from sup_case propperly placed'''
    fragment = [[] for _ in range(len(sup_case))]
    for i, gate in enumerate(sup_case):
        for _ in range(gate[1]):
            fragment[i].append('_')
        fragment[i].append('H')

    return fragment

def get_hsets(circuit):
    '''Return a list of Hadamard groups as a list of tuples (qubit, column)'''
    non_cancelled = []
    for i, qubit in enumerate(circuit):
        h_cols = [col for col, gate in enumerate(qubit) if gate == 'H']
        for j, h_col in enumerate(h_cols):
            if j % 2 == 0: # Not cancelled
                if j / 2 <= len(non_cancelled) - 1: # Exists data structure
                    non_cancelled[int(j / 2)].append((i,h_col))
                else:
                    non_cancelled.append([(i,h_col)])
    return non_cancelled

def get_hgates(col, col_no):
    '''Returns a list with <col_no> if the qubit has an H gate, -1 otherwise'''
    return [col_no if gate == 'H' else -1 for gate in col]

def get_cgates(col):
    '''Returns a a list with # of entity of each qubit and the entities as a list of dicts'''
    ents = []
    c_gates = [-1 for _ in range(len(col))]
    x_gates = []

    for i, gate in enumerate(col):
        if type(gate) == dict and 'CONTROL' in gate:
            new_ents = copy.deepcopy(ents)

            paired = False
            for j, ent in enumerate(ents):
                if i in ent.values() or gate['CONTROL'] in ent.keys():
                    new_ents[j][i] = gate['CONTROL']
                    c_gates[i] = j
                    paired = True

            if not paired:
                new_ents.append({i: gate['CONTROL']})
                c_gates[i] = len(new_ents) - 1

            ents = new_ents

        elif gate == 'X':
            x_gates.append(i)

    for x_qub in x_gates:
        for j, ent in enumerate(ents):
            if x_qub in ent.values():
                c_gates[x_qub] = j

    return c_gates, ents

def h_compare(first, second):
    '''Compares if the situation allows a control in an ENT can be held'''
    if first != -1:
        if second == -1:    # 1 ; 0 -> 1
            return first
        else:               # 1 ; 1 -> 0
            return -1
    else:
        if second == -1:    # 0 ; 0 -> 0
            return -1
        else:               # 0 ; 1 -> 1
            return second

def craft_ent(result, n_qubits):
    '''Returns the entanglement fragment for the given tuple (each item in found dict)'''
    fragment = [[] for _ in range(n_qubits)]
    ctrl_qubit = result[1][0][0]
    ctrl_col = int(result[0].split(':')[0])
    tgt_qubit = result[1][0][1][1]
    h_col = result[1][0][1][0]

    for _ in range(h_col):
        fragment[ctrl_qubit].append('_')
        fragment[tgt_qubit].append('_')

    fragment[ctrl_qubit].append('H')
    fragment[tgt_qubit].append('_')

    for _ in range(h_col + 1, ctrl_col):
        fragment[ctrl_qubit].append('_')
        fragment[tgt_qubit].append('_')

    fragment[ctrl_qubit].append({'CONTROL': tgt_qubit})
    fragment[tgt_qubit].append('X')

    return ctrl_qubit, h_col, fragment

class PatternFinder:
    '''Class for finding pattern matches for the circuit given as attribute'''
    def __init__(self, circuit: str):
        self.circuit = eval(circuit)
        self.final_results = {'INI': {}, 'SUP': {}, 'ENT': {}, 'ORA': {}}

    def find_oracle(self):
        '''Look for oracle by searching in dictionaries' keys'''
        matches = {} # Tuples {Count: (qubit_no, column_no, fragment)}
        count = 0

        for i, qubit in enumerate(self.circuit):
            for j, gate in enumerate(qubit):
                if type(gate) == dict and "ORACLE" in gate.keys():
                    matches[count] = (i,j, json.dumps(get_oracle(i,j, self.circuit)), 100.00)
                    count += 1

        return {'ORA': matches}

    def find_initialization(self):
        '''Looks for Pauli Gates at the beginning of the circuit'''
        matches = {}
        count = 0

        for i, qubit in enumerate(self.circuit):
            pauli_col = [-1,-1]
            for j, gate in enumerate(qubit):
                # Discard gate ifs
                if type(gate) == dict:
                    break

                # Pattern find decission tree
                if gate == '_':
                    continue
                elif gate in {'X','Y','Z'}:
                    if is_target(i, [row[j] for row in self.circuit]):
                        break

                    if pauli_col[0] == -1:
                        pauli_col = [j,j]
                    else:
                        pauli_col[1] += 1
                else: # Other gate
                    break

            # Add match if found
            if pauli_col != [-1,-1]:
                matches[count] = (i,pauli_col[0],
                    json.dumps([self.circuit[i][pauli_col[0] : pauli_col[1] + 1]]), 100.00)
                count += 1

        return {'INI': matches}

    def find_superposition(self):
        '''Look for an uniform superposition creation pattern'''
        matches = {}
        count = 0

        potential = get_hsets(self.circuit)

        # Check all qubits have H gate
        for case in potential:
            if len(case) == len(self.circuit): # All qubits
                matches[count] = (case[0][0], case[0][1], json.dumps(fill_hadamards(case)), 100.00)
                count += 1

        return {'SUP': matches}

    def find_entanglement(self):
        '''Look for entanglement pattern appearances'''
        trans = transpose_nonsquare(self.circuit)
        ready = [-1 for _ in range(len(self.circuit))]
        found = {}
        # found = { '<col_no>:<ctrl_ent_id>' : [(<ctrl_qubit>, (<H_col>, <ctrl_tgt_qubit>)), ...] }

        # 1) Find Entanglements
        for c, col in enumerate(trans):
            h_gates = get_hgates(col, c)
            ready = [h_compare(ready[i], h_gates[i]) for i in range(len(col))]
            c_gates, entities = get_cgates(col)

            if c_gates != [-1 for _ in range(len(self.circuit))]:
                for i in range(len(self.circuit)):
                    if ready[i] != -1 and c_gates[i] != -1:
                        if f'{c}:{c_gates[i]}' in found.keys():
                            # Already found entanglement expansion
                            found[f'{c}:{c_gates[i]}'].append((i,
                                                    (ready[i], entities[c_gates[i]][i])))
                        else:
                            found[f'{c}:{c_gates[i]}'] = [(i, (ready[i], entities[c_gates[i]][i]))]

        # 2) Build the result
        matches = {}
        count = 0
        for match in found.items():
            qubit_no, col_no, fragment = craft_ent(match, len(self.circuit))
            matches[count] = (qubit_no, col_no, json.dumps(fragment), 100.00)
            count += 1

        return {'ENT': matches}


def main(circuit):
    '''Main method for parallelizing the execution for pattern finding'''
    final_matches = {}
    finder = PatternFinder(circuit)
    result_keys = ['INI', 'SUP', 'ENT', 'ORA']
    finder_methods = [
        finder.find_initialization,
        finder.find_superposition,
        finder.find_entanglement,
        finder.find_oracle
    ]

    # Thread order: Initialization, Superposition, Entanglement, Oracle
    pool = multiprocessing.Pool(processes=len(result_keys))

    async_results = []
    for method in finder_methods:
        async_results.append(pool.apply_async(method))

    for result in async_results:
        final_matches.update(result.get())

    print(final_matches)

if __name__ == '__main__':
    main('[["X","H"],["Y","S","H"],[{"ORACLE":1},"H"]]')
