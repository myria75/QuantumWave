'''Module for the implementation for an automaton-based approach for pattern finding'''

# The _Record_ variable stores a Matrix with the following structure:
#   - ROWS: Qubit Number
#   - COLUMNS: Variable Index = {P,H,C}
#   - ITEMS: List of Gate tuples = [(Gate_Name, Col_Number)]
#
# By this way, if we have the indexation Record[0][P_INDEX] = [('X',0), ('Y',2)] means:
#   - The Qubit #0 has Pauli Gates, X and Y in columns 0 and 2 (respectively)
#
# This will allow processing the appearance (or not) of a pattern and the gates
# that composes it.

# pylint: disable=E0401
import re
import logging
from QCPDWeb.src.patterns import Match
# pylint: enable=E0401
#from patterns import Match

logging.basicConfig(format='%(asctime)s (%(levelname)s): %(message)s', level= logging.INFO)

ERROR_NO = 1
OKAY_NO = 0
PAULI_R = re.compile(r'X|Y|Z')
ORACLE_R = re.compile(r'O\d+')
CONTROL_R = re.compile(r'C\d+')
TARGET_R = re.compile(r'(T\d+(X|Y|Z|S|s|T|t|R[XYZ1]|I|M|_|H|([CO]\d+)))')
REM = '_'
H = 'H'
END_CHAR = '&'
NEXT_COL = '#'
LAMBDA = 'λ'
STACK_ALFABET = {
    'INI': 'I',
    'SUP': 'S',
    'ENT': 'E',
    'ENT0': 'ε',
    'ENT0F': 'ξ',
    'ORA': 'O',
    'FIRST': '$'
}

def true_control(ctrl_ent_dict):
    '''True if the entanglement has at least one single control gate'''
    for control in ctrl_ent_dict:
        if control[2][0] != 'T':
            return True
    return False

def search_controls(column):
    '''Returns a list of tuples with (ctrl_qubit, tgt_qubit) for the given column'''
    controls = []
    for qubit, gate in enumerate(column):
        if type(gate) == dict and 'CONTROL' in gate.keys():
            controls.append((qubit, gate['CONTROL']))
    return controls

def is_target(controls, candidate_qubit):
    '''Returns whether a gate is target for a control in the column'''
    for control in controls:
        if control[1] == candidate_qubit:
            return control
    return None

def adapt(circuit_list):
    '''Converts a circuit QPainter JSON format to compressed string for DFA'''
    compressed = ''

    for column in circuit_list:
        col_comp = ''
        controls = search_controls(column)
        for qubit, gate in enumerate(column):
            entity = is_target(controls, qubit)
            if entity is not None:
                col_comp += f'T{entity[0]}'
            if type(gate) == str:
                if gate == REM:
                    col_comp += '_'
                elif PAULI_R.search(gate) is not None:
                    if gate[0] != 'R':
                        col_comp += gate
                    else:
                        col_comp += '_'
                elif gate == H:
                    col_comp += gate
                else:
                    col_comp += '_'
            elif type(gate) == dict:
                if 'ORACLE' in gate.keys():
                    col_comp += f'O{gate["ORACLE"]}'
                elif 'CONTROL' in gate.keys():
                    col_comp += f'C{gate["CONTROL"]}'
                else:
                    col_comp += '_'

        compressed += (col_comp + '#')

    return compressed

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

def tuplist_to_qubdict(tuplist):
    '''Converts a list of tuples into a dictionary with qubit numbers as keys'''
    qubdict = {}
    for gate in tuplist:
        if gate[0] not in qubdict.keys():
            qubdict[gate[0]] = [(gate[2], gate[1])]
        else:
            qubdict[gate[0]].append((gate[2], gate[1]))
    return qubdict

def plain(matrix):
    '''Plains a matrix in a single one'''
    plained = []
    for i, row in enumerate(matrix):
        for item in row: # item = (gate_name, col)
            plained.append((i, item[1], item[0]))
    return plained

def count_gates(circuit_dict):
    '''Returns the number of qubits with one or more gate/s'''
    count = 0
    for qubit in circuit_dict:
        if len(qubit) >= 1:
            count += 1

    return count

def unpaired_hadamards(h_cols):
    '''Returns the number of unpaired (-1) H gates in H columns list'''
    unpaired = 0
    for hada in h_cols:
        if hada == -1:
            unpaired += 1
    return unpaired

def first_pairing_list(all_lists, qubit_no):
    '''Returns the index of the first available pairing list (-1 if not)'''
    for index, pairing in enumerate(all_lists):
        if pairing[qubit_no] == -1:
            return index

    return -1

def search_hadamard(pair_list):
    '''Returns a list with indices for hadamard gates'''
    indices = []
    for index, gate in enumerate(pair_list):
        if gate != -1:
            indices.append(index)

    return indices

def ent_to_qubdict(all_gates, circuit):
    '''Returns an appropriate qubit dictionary from the entanglement list of gates'''
    fragment = {}
    for i in range(len(circuit)):
        fragment[i] = []

    for gate in all_gates:
        new_gate = None
        inner_target = False
        if gate[2][0] == 'T':
            digits = int(re.findall(r'\d+', gate[2])[0])
            next_gate = TARGET_R.findall(gate[2])
            if next_gate[0][1][0] == 'C':
                inner_target = True
            else:
                new_gate = (next_gate[0][1], gate[1])
        if gate[2][0] == 'C' or inner_target:
            digits = int(re.findall(r'\d+', (gate[2] if not inner_target else next_gate[0][1]))[0])
            new_gate = ({'CONTROL':digits}, gate[1])
        if gate[2][0] == 'H':
            new_gate = ('H', gate[1])
        fragment[gate[0]].append(new_gate)
    return fragment

def is_controlled(column, gate_qub):
    '''Method for checking whether the gate in the told qubit is controlled '''
    for gate in column:
        if type(gate) == dict and 'CONTROL' in gate.keys():
            if gate['CONTROL'] == gate_qub: # Gate is controlled
                return True

    return False

class StateMachine:
    '''State Machine for searching potential matches of 4 patterns'''
    def __init__(self):
        self.circuit = ''
        self.n_qubits = 0
        self.pos = -1
        self.real_pos = -1
        self.stack = []
        self.verbose = False
        self.checker = None
        self.gate = None

    @property
    def qubit_no(self):
        '''Returns the current qubit number'''
        return self.real_pos % self.n_qubits

    @property
    def col_no(self):
        '''Returns the current column number'''
        return self.real_pos // self.n_qubits

    @property
    def non_sup(self):
        '''Returns the current number of non superposed qubits'''
        return self.checker.non_sup

    @property
    def found(self):
        '''Returns the current exact found patterns'''
        return self.checker.found
        ### Found DA Format ###
        # Once the PDA has finished the execution, the found property
        # can be consulted. It defines a Dictionary with four keys:
        #   - KEYS: {'INI', 'SUP', 'ENT', ORA'}
        # Each pair has as value a list of the found matches in the
        # given circuit.

    def start(self, circuit_str, verbose=False):
        '''Starts an execution of the automaton with the given circuit (QPainter style).
        It prepares all the attributes for a correct execution of the PDA, launches it,
        and shows whether the execution was correct or not. The matches should be accessed
        in the sm.found property'''
        # Initialization
        self.verbose = verbose
        circuit_list = eval(circuit_str)
        self.n_qubits = len(circuit_list)
        transposed = transpose_nonsquare(circuit_list)
        if verbose:
            print(f'[PEPD-PDA] Processing Circuit: {adapt(transposed)}\n')
            print('### TRANSITION REPORT ###')
        self.circuit = adapt(transposed) + END_CHAR
        self.checker = Checker(circuit_list)
        self.stack = [STACK_ALFABET['FIRST']]

        # Execution
        results = self._s0()

        # Reseting
        self.pos = -1
        self.real_pos = -1

        return results

    def _next(self):
        '''Method for getting the next gate in the compressed circuit string'''
        self.pos += 1
        self.real_pos += 1
        try:
            # next_char = self.gate
            next_char = self.circuit[self.pos]
        except IndexError:
            return '&'

        if next_char == 'O':
            self.pos += 1
            oracle_len = self.circuit[self.pos]
            self.pos += 1
            while self.circuit[self.pos].isdigit():
                oracle_len += self.circuit[self.pos]
                self.pos += 1
            self.pos -= 1
            next_char += oracle_len
        elif next_char == 'C':
            self.pos += 1
            target = self.circuit[self.pos]
            self.pos += 1
            while self.circuit[self.pos].isdigit():
                target += self.circuit[self.pos]
                self.pos += 1
            self.pos -= 1
            next_char += target

        elif next_char == 'T':
            contin = self.circuit[self.pos:]
            whole = TARGET_R.findall(contin)[0]
            self.pos += len(whole[0]) - 1
            next_char = whole[0]

        elif next_char == NEXT_COL:
            self.real_pos -= 1

        return next_char

    def _s0(self):
        '''State S0: New Column'''

        # Inform
        if self.verbose:
            print('S0')

        # Task
        pass

        # Transition
        self.gate = self._next()
        if self.verbose:
            print(f'S0 --{self.gate}-> ', end='')
        if TARGET_R.search(self.gate) is not None:
            if self.stack[-1] == STACK_ALFABET['ENT'] or\
                STACK_ALFABET['ENT'] in self.stack:
                return self._s7()
            else:
                return self._s4()
        elif PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == REM:
            # For every value for stack
            return self._s4()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif ORACLE_R.search(self.gate) is not None:
            # For every value for stack
            return self._s3()
        elif CONTROL_R.search(self.gate) is not None:
            if self.stack[-1] == STACK_ALFABET['ENT0'] or\
                STACK_ALFABET['ENT'] in self.stack:
                return self._s7()
            else:
                return self._s4()
        elif self.gate == END_CHAR:
            # For every value for stack
            return self._s8()
        elif self.gate == NEXT_COL:
            # For every value for stack
            return ERROR_NO

    def _s1(self):
        '''State S1: "INI" potentially found'''
        # Inform
        if self.verbose:
            print('S1')

        # Task
        if self.checker.check_ini((self.qubit_no, self.col_no, self.gate)):
            stack_top = self.stack.pop()
            if stack_top in (STACK_ALFABET['ENT0'], STACK_ALFABET['ENT0F']):
                self.stack.append(STACK_ALFABET['INI'])
                self.stack.append(stack_top)
            else:
                self.stack.append(stack_top)
                self.stack.append(STACK_ALFABET['INI'])
            if self.verbose:
                print('[AEPD-Checker] Initialization Pattern found/updated!')

        # Transitions
        ## Lambda Transitions
        if self.stack[-1] == STACK_ALFABET['ENT0']:
            if self.verbose:
                print(f'S1 --{LAMBDA}-> ', end='')
            return self._s5()
        elif self.stack[-1] == STACK_ALFABET['ENT0F']:
            if self.verbose:
                print(f'S1 --{LAMBDA}-> ', end='')
            return self._s6()

        ## Non-Lambda Transitions
        self.gate = self._next()
        if self.verbose:
            print(f'S1 --{self.gate}-> ', end='')
        if PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == REM:
            # For every value for stack
            return self._s4()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif ORACLE_R.search(self.gate) is not None:
            # For every value for stack
            return self._s3()
        elif self.gate == NEXT_COL:
            # For every value for stack
            return self._s0()
        elif self.gate == END_CHAR:
            # For every value for stack
            return ERROR_NO

    def _s2(self):
        '''State S2: "SUP" potentially found'''
        # Inform
        if self.verbose:
            print('S2')

        # Task
        if self.checker.check_sup((self.qubit_no, self.col_no, self.gate)):
            stack_top = self.stack.pop()
            if stack_top != STACK_ALFABET['ENT0'] or \
                    stack_top != STACK_ALFABET['ENT0F']:
                self.stack.append(stack_top)
            self.stack.append(STACK_ALFABET['SUP'])
            if self.verbose:
                print('[AEPD-Checker] Superposition pattern found!')

        # Transitions
        ## Lambda Transitions
        if self.stack[-1] != STACK_ALFABET['SUP']:
            if self.verbose:
                print(f'S2 --{LAMBDA}-> ', end='')
            return self._s5()
        elif self.stack[-1] == STACK_ALFABET['ENT0F']:
            if self.verbose:
                print(f'S2 --{LAMBDA}-> ', end='')
            return self._s6()

        ## Non-Lambda Transitions
        self.gate = self._next()
        if self.verbose:
            print(f'S2 --{self.gate}-> ', end='')
        if PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == REM:
            # For every value for stack
            return self._s4()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif ORACLE_R.search(self.gate) is not None:
            # For every value for stack
            return self._s3()
        elif CONTROL_R.search(self.gate) is not None:
            return self._s5()
        elif self.gate == NEXT_COL:
            # For every value for stack
            return self._s0()
        elif self.gate == END_CHAR:
            # For every value for stack
            return ERROR_NO

    def _s3(self):
        '''State S3: "ORA" potentially found'''
        # Inform
        if self.verbose:
            print('S3')

        # Task
        if self.checker.check_ora((self.qubit_no, self.col_no, self.gate)):
            stack_top = self.stack.pop()
            if stack_top in (STACK_ALFABET['ENT0'], STACK_ALFABET['ENT0F']):
                self.stack.append(STACK_ALFABET['ORA'])
                self.stack.append(stack_top)
            else:
                self.stack.append(stack_top)
                self.stack.append(STACK_ALFABET['ORA'])
            if self.verbose:
                print('[AEPD-Checker] Oracle pattern found!')

        # Transitions
        ## Lambda Transitions
        if self.stack[-1] == STACK_ALFABET['ENT0']:
            if self.verbose:
                print(f'S2 --{LAMBDA}-> ', end='')
            return self._s5()
        elif self.stack[-1] == STACK_ALFABET['ENT0F']:
            if self.verbose:
                print(f'S2 --{LAMBDA}-> ', end='')
            return self._s6()

        ## Non-Lambda Transitions
        self.gate = self._next()
        if self.verbose:
            print(f'S3 --{self.gate}-> ', end='')
        if PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == REM:
            # For every value for stack
            return self._s4()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif ORACLE_R.search(self.gate) is not None:
            # For every value for stack
            return self._s3()
        elif self.gate == NEXT_COL:
            # For every value for stack
            return self._s0()
        elif self.gate == END_CHAR:
            # For every value for stack
            return ERROR_NO

    def _s4(self):
        '''State S4: Remaining gate found [Neutral state]'''
        # Inform
        if self.verbose:
            print('S4')

        # Task
        pass

        # Transitions
        ## Lambda Transitions
        if STACK_ALFABET['ENT'] in self.stack:
            if self.verbose:
                print(f'S4 --{LAMBDA}-> ', end='')
            self.stack.append(STACK_ALFABET['ENT0F'])
            return self._s6()

        ## Non Lambda Transitions
        self.gate = self._next()
        if self.verbose:
            print(f'S4 --{self.gate}-> ', end='')
        if ORACLE_R.search(self.gate) is not None:
            # For every value for stack
            return self._s3()
        if TARGET_R.search(self.gate) is not None:
            # For every value for stack
            return self._s4()
        elif CONTROL_R.search(self.gate) is not None:
            # For every value for stack
            return self._s4()
        elif PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == REM:
            # For every value for stack
            return self._s4()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif self.gate == NEXT_COL:
            # For every value for stack
            return self._s0()
        elif self.gate == END_CHAR:
            # For every value for stack
            return ERROR_NO

    def _s5(self):
        '''State S5: "ENT0" Atomic Part found'''
        # Inform
        if self.verbose:
            print('S5')

        # Task
        if self.checker.check_ent0():
            stack_top = self.stack.pop()
            if stack_top == STACK_ALFABET['ENT0']:
                self.stack.append(stack_top)
            else:
                self.stack.append(stack_top)
                self.stack.append(STACK_ALFABET['ENT0'])

        # Transitions
        self.gate = self._next()
        if self.verbose:
            print(f'S5 --{self.gate}-> ', end='')
        if PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == REM:
            stack_top = self.stack.pop()
            if stack_top == STACK_ALFABET['ENT0']:
                return self._s5()
            else:
                return self._s4()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif ORACLE_R.search(self.gate):
            # For every value for stack
            return self._s3()
        elif self.gate == NEXT_COL:
            if self.stack[-1] == STACK_ALFABET['ENT0']:
                return self._s6()
            else:
                return self._s0()
        elif self.gate == END_CHAR:
            # For every value for stack
            return self._s8()

    def _s6(self):
        '''State S6: "ENT0F" found, looking for controlled'''
        # Inform
        if self.verbose:
            print('S6')

        # Task
        if self.gate == NEXT_COL:
            stack_top = self.stack.pop()
            if stack_top == STACK_ALFABET['ENT0']:
                self.stack.append(STACK_ALFABET['ENT0F'])
            else:
                self.stack.append(stack_top)

        # Transition
        self.gate = self._next()
        if self.verbose:
            print(f'S6 --{self.gate}-> ', end='')
        if TARGET_R.search(self.gate) is not None:
            if self.stack[-1] == STACK_ALFABET['ENT0F']:
                return self._s7()
            else:
                return ERROR_NO
        elif self.gate == REM:
            # For every value for stack
            return self._s6()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif ORACLE_R.search(self.gate) is not None:
            # For every value for stack
            return self._s3()
        elif CONTROL_R.search(self.gate) is not None:
            # For every value for stack
            return self._s7()
        elif PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == NEXT_COL:
            # For every value for stack
            return self._s6()
        elif self.gate == END_CHAR:
            # For every value for stack
            return self._s8()

    def _s7(self):
        '''State S7: "ENT" potentially found'''
        # Inform
        if self.verbose:
            print('S7')

        # Task
        if self.checker.check_ent((self.qubit_no, self.col_no, self.gate)):
            stack_top = self.stack.pop()
            if stack_top == STACK_ALFABET['ENT0F']:
                self.stack.append(STACK_ALFABET['ENT'])
                if self.verbose:
                    print('[AEPD-Checker] Entanglement pattern found!')
            else:
                self.stack.append(stack_top)

        # Transition
        self.gate = self._next()
        if self.verbose:
            print(f'S7 --{self.gate}-> ', end='')
        if self.gate == REM:
            if self.stack[-1] == STACK_ALFABET['ENT0F']:
                return self._s7()
            elif self.stack[-1] == STACK_ALFABET['ENT']:
                return self._s4()
        elif self.gate == H:
            # For every value for stack
            return self._s2()
        elif ORACLE_R.search(self.gate) is not None:
            # For every value for stack
            return self._s3()
        elif TARGET_R.search(self.gate) is not None:
            if self.stack[-1] == STACK_ALFABET['ENT0F'] or\
                STACK_ALFABET['ENT'] in self.stack:
                return self._s7()
            elif self.stack[-1] == STACK_ALFABET['ENT']:
                return self._s4()
        elif CONTROL_R.search(self.gate) is not None:
            if self.stack[-1] == STACK_ALFABET['ENT0F'] or\
                STACK_ALFABET['ENT'] in self.stack:
                return self._s7()
            elif self.stack[-1] == STACK_ALFABET['ENT']:
                return self._s4()
        elif PAULI_R.search(self.gate) is not None:
            # For every value for stack
            return self._s1()
        elif self.gate == NEXT_COL:
            if self.stack[-1] == STACK_ALFABET['ENT0F']:
                return self._s7()
            elif self.stack[-1] == STACK_ALFABET['ENT']:
                return self._s0()
        elif self.gate == END_CHAR:
            # For every value for stack
            return self._s8()

    def _s8(self):
        '''State S8: Final State'''
        # Inform
        if self.verbose:
            print('S8')

        # Task --> Print Found Patterns
        if self.verbose:
            print('[PEPD-PDA] Search Finished')
        report = '### PATTERN REPORT ###\n'
        counter = 0
        for pat_type, pat_matches in self.found.items():
            report += f'- {pat_type}:\n'
            for match in pat_matches:
                report += f'\tPat.{counter} --> {match.get_fragment()}\n'
                counter += 1

        # Transition
        return OKAY_NO

class Checker:
    '''Exact pattern checking class (given a gate as [qubit, col, gate_name]).'''
    def __init__(self, circuit_list):
        self.circuit = circuit_list
        self.non_sup = 1 # Proportion percentage
        self.ini = [[] for _ in self.circuit] # Pauli Gates
        self.ini.append([False for _ in range(len(self.circuit))]) # Init. Finished Qubits
        self.sup = [[] for _ in self.circuit] # Hadamard Gates
        self.sup.append([[-1 for _ in self.circuit]]) # Concurrent H Appearances
        self.ent = [[],{}] # ENT control and target qubits for ENT0 and actual ENT
        #### self.ent component explanation ####
        # - self.ent[0]: List for storing ENT0 potential future controls in ENT
        # - self.ent[1]: Dictionary with pairs:
        #       -> <column_number_controlled_gate>: {'CONTROL':[X0], 'TARGET':[X1]}
        # Where Xi = (<qubit_no>, <column_no>, <gate_name>)
        self.found = {
            'INI': [],
            'SUP': [],
            'ENT': [],
            'ORA': []
        }

    def _add(self, matrix, gate):
        '''Adds a gate into the Checker in adequate pattern matrix'''
        matrix[gate[0]].append((gate[2], gate[1])) # (Gate_name, Gate_col)
        matrix[gate[0]].sort(key= lambda tup: tup[1]) # Order gates in qubit by col

    def check_ini(self, gate):
        '''Checks whether the given gate results in/updates an initialization pattern'''
        self._add(self.ini, gate) # gate = (qubit, col, name)
        match = True
        if not self.ini[-1][gate[0]]: # Qubit not initialized
            i = 0
            j = gate[1]
            if len(self.ini[gate[0]]) == 1: # Only one Pauli
                i = 0
            else:
                penult = self.ini[gate[0]][-2] # More than one Pauli
                i = penult[1]

            critical = self.circuit[gate[0]][i:j+1] # Get critical range

            for mid_col, mid_gate in enumerate(critical):
                if mid_gate not in ['X','Y','Z','_','I']:
                    match = False
                    self.ini[-1][gate[0]] = True
                    break
                else:
                    if is_controlled([qubit[mid_col] for qubit in self.circuit], gate[0]):
                        match = False
                        self.ini[-1][gate[0]] = True
                        break
        else:
            match = False

        if match: # Match found
            if self.found['INI'] != []:
                self.found['INI'].pop(0)
            self.found['INI'].append(Match(tuplist_to_qubdict(plain(self.ini[:-1])),
                'Initialization'))

        return match

    def check_sup(self, gate):
        '''Checks whether the given gate results in a superposition pattern'''
        match = False
        self._add(self.sup, gate)

        index = first_pairing_list(self.sup[-1], gate[0])
        if index == -1: # New pairing list needed
            index = len(self.sup[-1])
            self.sup[-1].append([-1 for _ in self.circuit])
        self.sup[-1][index][gate[0]] = gate[1]

        paired = unpaired_hadamards(self.sup[-1][index])
        if paired == 0: # Whole "Column" paired
            if index % 2 == 0: # Not cancelled
                match_dict = {}
                for qubit, column in enumerate(self.sup[-1][index]):
                    match_dict[qubit] = [('H', column)]
                self.found['SUP'].append(Match(match_dict, 'Superposition'))
                match = True
            self.non_sup = 0
        else:
            self.non_sup = (len(self.circuit) - paired) / len(self.circuit)
        return match

    def check_ora(self, gate):
        '''Adds Oracle pattern instance to the found list (not potential, directly found)'''
        ora = re.findall(r'\d+', gate[2])
        ora_len = ora[-1]

        ora_gate = (gate[0], gate[1], gate[2], int(ora_len))
        self.found['ORA'].append(Match({ora_gate[0]:
                                    [(ora_gate[2], ora_gate[1], ora_gate[3])]},
                                'Oracle')) # qubit: (O, col len)
        return True

    def check_ent0(self):
        '''Checks if the ENT0 part exists'''
        match = False
        if len(self.sup[-1]) % 2 == 1: # Non cancelled
            superposed = search_hadamard(self.sup[-1][-1])
            if len(superposed) < len(self.sup[-1][-1]): # Not all paired
                self.ent[0] = superposed
                match = True
        return match

    def check_ent(self, gate):
        '''Checks whether the given gate results in an entanglement pattern'''
        match = False
        searched = CONTROL_R.findall(gate[2])

        if gate[1] not in list(self.ent[1].keys()):
            self.ent[1][gate[1]] = {'CONTROL':[], 'TARGET':[]}

        if searched != [] and gate[2][0] != 'T':
            if gate[0] in self.ent[0]:
                self.ent[1][gate[1]]['CONTROL'].append(gate)
        else:
            searched = TARGET_R.findall(gate[2])
            if searched != []:
                if gate[0] not in self.ent[0] and gate[2][-1] == 'X':
                    # The gate is not a controlled or if a controlled target, there is
                    # another non controlled gate
                    self.ent[1][gate[1]]['TARGET'].append(gate)
                elif gate[2][0] == 'T' and gate[0] in self.ent[0]:
                    self.ent[1][gate[1]]['CONTROL'].append(gate)

        if true_control(self.ent[1][gate[1]]['CONTROL']) and \
                self.ent[1][gate[1]]['TARGET'] != []:
            match = True
            # Get the qubit dictionary for the fragment
            hadamards = []
            for control in self.ent[1][gate[1]]['CONTROL']:
                hadamards.append((control[0],self.sup[control[0]][0][1],"H"))
            all_gates = hadamards + self.ent[1][gate[1]]['CONTROL'] + self.ent[1][gate[1]]['TARGET']
            fragment = ent_to_qubdict(all_gates, self.circuit)

            new_match = Match(fragment, 'Entanglement')
            if len(self.found['ENT']) > 0:
                for i, prev_match in enumerate(self.found['ENT']):
                    if prev_match.is_extensible(new_match):
                        self.found['ENT'][i] = new_match
                        return match
                    elif prev_match.equals(new_match):
                        return False
            self.found['ENT'].append(Match(fragment, 'Entanglement'))

        return match

if __name__ == '__main__':
    dfa = StateMachine()
    if dfa.start(
        '[["X","H",{"ORACLE":3},"H","X"],["Y","H","ORACLE2","H","Y"],' +\
            '["Z","H","ORACLE2","H","Z"]]', 
            verbose=True
        ) != 0:
        print('DFA returned an error')
    print(dfa.stack)
    print(dfa.found)
    # circuit_6 = [["H",{"CONTROL":1}],["H",{"CONTROL":3}],[],["_","X"]]
    # transposed = transpose_nonsquare(circuit_6)
    # print(f'Processing Circuit: {adapt(transposed)}')
