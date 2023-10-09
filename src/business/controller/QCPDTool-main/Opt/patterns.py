'''Module for defining the logic and data needed for each pattern match'''

def column_occ(row, col_no):
    '''Return the gate in the given column number within the row expressed as involved_gates'''
    for gate in row:
        if gate[1] == col_no:
            return gate[0]
    return '_'

def tuplist_to_gatelist(tuple_list):
    '''Converts a tuple list with [(<gate>, <col>), ...] in a list of gates [X,_,Y,...]-like'''
    gate_list = []
    max_col = max(tuple_list, key=lambda x: x[1])[1] # Max column for the qubit
    for i in range(max_col + 1):
        final_gate = column_occ(tuple_list, i)
        gate_list.append(final_gate)

    return gate_list

class Match:
    '''Class with the necessary data and methods defining a pattern match'''
    def __init__(self, involved_gates, pattern):
        self.gates = involved_gates
        self.pattern = pattern
        # Involved gates: Dict --> {
        # 'qubit_no': [(Gate_Name0, Col_no0), ..., (Gate_NameN, Col_noN)]
        # }

    def get_fragment(self):
        '''Method returning the pattern match fragment in the circuit as QPainter JSON format'''
        fragment = []

        if self.pattern == 'Oracle':
            # Get the oracle gate in self.gates
            ora_qubit = list(self.gates.keys())[0]
            oracle = self.gates[ora_qubit][0]

            fragment = [[] for _ in range(ora_qubit)]
            ora_row = ['_' for _ in range(oracle[1])]
            ora_row.append({'ORACLE': oracle[2]})
            fragment.append(ora_row)

            for _ in range(ora_qubit + 1, ora_qubit + oracle[2]):
                ora2_row = ['_' for _ in range(oracle[1])]
                ora2_row.append('ORACLE2')
                fragment.append(ora2_row)

        elif self.pattern == 'Initialization':
            last_qubit = list(self.gates.keys())[-1]
            for i in range(last_qubit + 1):
                row = []
                if i in self.gates.keys(): # Fill "row" if initialized
                    row = tuplist_to_gatelist(self.gates[i])

                fragment.append(row)

        elif self.pattern == 'Superposition':
            for key in self.gates:
                row = []
                for i in range(max([pair[1] for pair in self.gates[key]]) + 1):
                    current = self.gates[key]
                    row.append(column_occ(current, i))

                fragment.append(row)

        elif self.pattern == 'Entanglement':
            for key, value in self.gates.items():
                qubit = []
                if value != []:
                    for i in range(value[0][1]):
                        qubit.append('_')
                    actual_gates = [gate[1] for gate in value]
                    for column in range(value[0][1], value[-1][1] + 1):
                        if column in actual_gates:
                            qubit.append(column_occ(value, column))
                        else:
                            qubit.append('_')
                    # qubit.append(value[0][0])
                fragment.append(qubit)

        return fragment

    def add_gate(self, gate_name, qubit_no, col_no):
        '''Method for adding a gate in the fragment according to the gate Data Structure'''
        self.gates[qubit_no].append((gate_name, col_no))

    def is_extensible(self, new_candidate):
        '''Checks if new_candidate is an extension of the current Match'''
        if self.pattern != new_candidate.pattern:
            return False

        zipped_self = [gate for qubit in self.gates.values() for gate in qubit]
        zipped_new = [gate for qubit in new_candidate.gates.values() for gate in qubit]

        if len(zipped_self) >= len(zipped_new):
            return False

        for i in range(len(zipped_self)):
            if type(zipped_self[i]) == dict:
                if type(zipped_new[i]) != dict:
                    return False

                if list(zipped_self[i].keys())[0] !=\
                    list(zipped_new[i].keys())[0]:
                    return False
            else:
                if zipped_self[i][0] != zipped_new[i][0]:
                    return False

        return True

    def equals(self, new_candidate):
        '''Checks whether the new candidate is semantically the same as self'''
        zipped_self = [gate for qubit in self.gates.values() for gate in qubit]
        zipped_new = [gate for qubit in new_candidate.gates.values() for gate in qubit]

        if len(zipped_self) != len(zipped_new):
            return False

        for i in range(len(zipped_self)):
            if type(zipped_self[i][0]) == dict and\
                type(zipped_new[i][0]) == dict:
                val_prev = zipped_self[i][0].values()
                val_cand = zipped_new[i][0].values()

                if val_cand != val_prev:
                    # Different columns
                    return False

                self_keys = zipped_self[i][0].keys()
                new_keys = zipped_new[i][0].keys()
                if self_keys == new_keys:
                    if zipped_self[i][0][list(zipped_self[i][0].keys())[0]] !=\
                        zipped_new[i][0][list(zipped_new[i][0].keys())[0]]:
                        return False
                else:
                    return False

            else:
                if zipped_new[i][0] != zipped_self[i][0]:
                    return False

        return True

if __name__ == '__main__':
    gates = {'0': [('X', 0), ('H', 2)], '1': [('Y', 1)]}
    # match = Match(gates)
    # print(match.get_fragment())
