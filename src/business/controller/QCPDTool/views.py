
'''Piece of code from Sergio's TFG where we obtain the table of patterns including its errors'''

import json
import requests
from src.business.controller.QCPDTool.src import finder_sm as sm
from src.business.controller.QCPDTool.src import finder_sim as sim
import os
import configparser

ERR_PROCESSING = ('Processing Error',
                'An error ocurred when processing the circuit for searching patterns.' +\
                'The given circuit was well designed but its logic is not correct.' +\
                'Please make sure that the circuit is correctly designed.')
ERR_BLANKCIRCUIT = ('Circuit Error',
                    'The given circuit is blank. Please, try again with other circuit.')
ERR_CONNECTION = ('Connection Error',
                'Something went wrong when connecting with QPainter. QPainter server might ' +\
                'be down. Please, try again later when potential errors could be solved.')
ERR_CIRCUIT = ('Circuit Error',
              'The given circuit was not correctly written. Contrast your circuit\'s ' +\
              'syntax with the QPainter\'s Circuit syntax regarding your input JSON format.')
ERR_ANGLE = ('Rotation Angle Error',
            'The given angle format or data type in <X> is not correct. It must be a float ' +\
            'number (e.g. 3.14). Please, try again with a correct angle.')

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

QPAINTER_URL = eval(config.get('URL', 'qpainter'))
PATTERN_ACHRONYMS = {
    'INI': 'initialization',
    'ENT': 'entanglement',
    'ORA': 'oracle',
    'SUP': 'superposition'
}

# ## Front-end Matches DA Format ###
# The DA required by the front-end part for rendering the pattern matches is
# a Dictionary with the following pairs:
#   - Pairs: <Type_of_match>: Inner Dictionary
# Where:
#   a. <Type_of_match> is in {'entanglement','initialization','oracle','superposition','uncompute'}
#   b. Inner Dictionary has the pairs:
#       - Pairs: <Match_id>: <Match_tuple>
#   Where:
#       i. <Match_id> is an integer used as identifier.
#       ii. <Match_tuple> is a tuple with the info needed for locate the match. More specifically:
#           - (qubit_no, column_no, fragment)

def sm_to_front(pda_matches):
    '''Translates the matches format given from the PDA Module to the format
    needed for the HTML rendering process'''
    front_match = {}
    counter_id = 0
    for pat_kind, matches in pda_matches.items():
        kind_dict = {}
        for match in matches:

            first_qubit = 0
            for qubit, gate_list in match.gates.items():
                if gate_list != []:
                    first_qubit = qubit

            first_column = match.gates[first_qubit][0][1]

            match_tuple = (first_qubit, first_column, json.dumps(match.get_fragment()))
            kind_dict[counter_id] = match_tuple
            counter_id += 1
        front_match[PATTERN_ACHRONYMS[pat_kind]] = kind_dict

    return front_match

def circuit_ok(response):
    '''Process QPainter response and return proper error info if needed'''
    err_title = err_msg = None
    if response.status_code == requests.codes.ok:
        if not response.json()['correct']:
            err_title = ERR_CIRCUIT[0]
            err_msg = ERR_CIRCUIT[1]
            return err_title, err_msg
    else:
        err_title = ERR_CONNECTION[0]
        err_msg = ERR_CONNECTION[1]
        return err_title, err_msg

    return err_title, err_msg if err_title is not None else None

def get_patterns():
    '''Return list of the wanted patterns'''
    manager = db.PatternManager()
    pat_list = manager.read_all()
    return pat_list

def contain_oracles(input_circ):
    '''Returns true if the circuit has at least one oracle. False otherwise'''
    for qubit in input_circ:
        for gate in qubit:
            if isinstance(gate, dict) and 'ORACLE' in gate:
                return True
    return False

def get_oracles(input_circ):
    '''Returns a list with oracles as dictionaries'''
    oracles = []
    for qubit in input_circ:
        for gate in qubit:
            if isinstance(gate, dict) and 'ORACLE' in gate:
                oracles.append(gate)
    return oracles

def contain_rotation(input_circ):
    '''Returns true if the circuit has at least one rotation gate. False otherwise'''
    for qubit in input_circ:
        if 'RX' in qubit or 'RY' in qubit or\
           'RZ' in qubit or 'R1' in qubit:
            return True
    return False


def generate_pattern(input_circ):
    context = {}

    # 1) Check empty circuit
    if input_circ == '':
        context['err_title'] = ERR_BLANKCIRCUIT[0]
        context['err_msg'] = ERR_BLANKCIRCUIT[1]
        return context

    if input_circ == '[]' or input_circ == '{}':
        context['err_title'] = ERR_BLANKCIRCUIT[0]
        context['err_msg'] = ERR_BLANKCIRCUIT[1]
        return context

    # 2) Initial Input Checking
    ## 2.1) Circuit string checking
    #
    try:
        response = requests.get(f'{QPAINTER_URL}check/{input_circ}')
    except Exception:   #if couldn't connect, throws an error
        context['err_title'] = ERR_CONNECTION[0]
        context['err_msg'] = ERR_CONNECTION[1]
        return context
    err_info = circuit_ok(response)

    if err_info[0] is not None: # Incorrect Circuit
        context['err_title'] = err_info[0]
        context['err_msg'] = err_info[1]
        return context

    # 3) Circuit Processing
    # 3.1) SM Processing
    sm_finder = sm.StateMachine()
    if sm_finder.start(input_circ, verbose=False) != 0:
        print('DFA returned an error')
        context['err_title'] = ERR_PROCESSING[0]
        context['err_msg'] = ERR_PROCESSING[1]
        return context
    sm_matches = sm_finder.found
    front_matches = sm_to_front(sm_matches)

    # 3.2) Simulator Processing
    has_uncompute = sim.main(eval(input_circ))
    if has_uncompute == 1: # Uncompute pattern found
        patt_id = sum(len(matches) for matches in front_matches.values())
        patt_tuple = (0,0,input_circ)
        front_matches['uncompute'] = {patt_id: patt_tuple}
    context = front_matches

    return context