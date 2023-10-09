'''
    Module for defining the Supervisor class in charge of 
    giving warnings and comments based on the results
'''

INIT_WARN = ('Initialization',
        'The Initialization pattern is used mainly for encoding the ' +\
        'input of a quantum algorithm in qubits for further computations. ' +\
        'In the given circuit Initialization was not used. Make sure you '+\
        'actually don\'t need it for your problem.')
SUPER_WARN = ('Superposition',
        'The Superposition pattern is one of the main advantages of '+\
        'quantum circuit model. It allows superposing in the state all the '+\
        'possible values. In your circuit <i>only the <X> percent of the qubits '+\
        'are superposed<i>. Is this proportion enough for your problem?')
UNCOMP_WARN = ('Uncompute',
        'The Uncompute pattern makes the qubit return to the initial state ' +\
        'after certain gates are applied so that it can be reused later. In your '+\
        'circuit, a symmetry exists but the initial state is not the same ' +\
        'as the final one. Consider the possibility of using this pattern.')


class Supervisor:
    '''Supervisor Class with the considerations for the current list of warnings'''
    def __init__(self, uncomp_out, init_list, super_propor):
        self.uncomp = uncomp_out
        self.init = init_list
        self.super = super_propor

    def check_init(self):
        '''Investigates the init_list for extracting a warning conclusion'''
        if self.init == {}: # No initialization pattern found
            return INIT_WARN
        return None

    def check_super(self):
        '''Investigates the super_date for extracting a warning conclusion'''
        if self.super > 0.5 and self.super < 1.0: # More than half of qubits are superposed
            return (SUPER_WARN[0], SUPER_WARN[1].replace('<X>', f'{(self.super*100):.2f}'))
        return None

    def check_uncom(self):
        '''Investigates the uncomp_out for extracting a warning conclusion'''
        if self.uncomp == 2:
            return UNCOMP_WARN
        return None

    def check_all(self):
        '''Checks all the possibilities and returns a list of conclusions'''
        warnings = []
        results = [self.check_init(),
                   self.check_super(),
                   self.check_uncom()]

        for result in results:
            if result is not None:
                warnings.append(result)

        return warnings
