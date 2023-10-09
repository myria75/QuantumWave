'''Script for comparing the execution time of the SM-based approach and the parallel approach'''

import time
from finder_par import main
from finder_sm import StateMachine

# Output Log File
RESULTS_LOG = open('test_results.txt', 'w', encoding='utf-8')

# Circuit examples for measurements
CIRCUIT48 = '[["H","_","_","_","_","_",{"CONTROL":1},{"CONTROL":2},"_",{"CONTROL":2},"_",' +\
    '{"CONTROL":1},{"CONTROL":2},"_",{"CONTROL":2},"_","X",{"CONTROL":1},{"CONTROL":2},"_",' +\
    '{"CONTROL":2},"_",{"CONTROL":1},{"CONTROL":2},"_",{"CONTROL":2},"_",{"CONTROL":3}],' +\
    '["H",{"CONTROL":2},"_",{"CONTROL":2},"_","X",{"CONTROL":2},"_","_","_","_",{"CONTROL":2},' +\
    '"_","_","_","_","_",{"CONTROL":2},"_","_","_","_",{"CONTROL":2},"_","_","_","_","_","H",' +\
    '"MEASURE"],["_","X","RY","X","RY","_","X","X","RY","X","RY","X","X","RY","X","RY","_","X",' +\
    '"X","RY","X","RY","X","X","RY","X","RY"],["_","_","_","_","_","_","_","_","_","_","_","_",' +\
    '"_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","X","_","MEASURE"]]'
CIRCUIT44 = '[["H",{"CONTROL":2},{"CONTROL":1},"_",{"CONTROL":1},"_","_",{"CONTROL":2},' +\
    '{"CONTROL":1},"_",{"CONTROL":1},"_","X",{"CONTROL":2},{"CONTROL":1},"_",{"CONTROL":1},' +\
    '"_","_",{"CONTROL":2},{"CONTROL":1},"_",{"CONTROL":1},"_","MEASURE"],["H","_","X",' +\
    '{"CONTROL":2},"X",{"CONTROL":2},"X","_","X",{"CONTROL":2},"X",{"CONTROL":2},"X","_","X",' +\
    '{"CONTROL":2},"X",{"CONTROL":2},"X","_","X",{"CONTROL":2},"X",{"CONTROL":2},"MEASURE"],' +\
    '["_","RY","_","RY","_","RY","_","RY","_","RY","_","RY","_","RY","_","RY","_","RY","_","RY",' +\
    '"_","RY","_","RY","MEASURE"]]'
circuits = [CIRCUIT48, CIRCUIT44]

# Time measuring loop
def time_test(circuits):
    '''Main method for launching the time test execution with the list as input'''
    RESULTS_LOG.write('>>> Input Circuit for Tests <<<\n'+\
                      f'Circuit 1: {circuits[0]}\n'+\
                      f'Circuit 2: {circuits[1]}\n\n')

    for i, circuit in enumerate(circuits):
        print(f'### EXECUTION OF CIRCUIT {i} ###')

        # SM-Based approach execution
        print('> SM-Based approach in progress')
        state_machine = StateMachine()
        init_sm_time = time.time()
        result_code = state_machine.start(circuit)
        end_sm_time = time.time()

        if result_code != 0:
            print(f'\t--> Execution of circuit #{i} returned 0 code')

        # Parallel approach execution
        print('> Parallel approach in progress')
        init_par_time = time.time()
        main(circuit)
        end_par_time = time.time()

        # Iteration Result
        sm_time = end_sm_time - init_sm_time
        par_time = end_par_time - init_par_time
        print(f'### CIRCUIT {i} REPORT ###')
        print(f'- SM-based time: {sm_time}')
        print(f'- Parallel time: {par_time}\n')

        # Logging results
        RESULTS_LOG.write(f'### CIRCUIT {i} REPORT ###' +\
                          f'\n- SM-based time: {sm_time}' +\
                          f'\n- Parallel time: {par_time}\n\n')

if __name__ == '__main__':
    print('-> Preparing test to be launched...')
    time_test(circuits)
    print('-> Tests finished correctly. Results are written in file "test_results.txt"')
