'''Module for rendering and processing respective petitions to the BackEnd'''
import json
import db_manage as db
from django.shortcuts import render
import requests
from QCPDWeb.src import finder_sm as sm
from QCPDWeb.src import finder_sim as sim
from QCPDWeb.src import supervisor as sup

ERR_PROCESSING = ('Processing Error',
                'An error ocurred when processing the circuit for searching patterns.' +\
                'The given circuit was well designed but its logic is not correct.' +\
                'Please make sure that the circuit is correctly designed.')
ERR_CONNECTION = ('Connection Error',
                'Something went wrong when connecting with QPainter. QPainter server might ' +\
                'be down. Please, try again later when potential errors could be solved.')
ERR_CIRCUIT = ('Circuit Error',
              'The given circuit was not correctly written. Contrast your circuit\'s ' +\
              'syntax with the QPainter\'s Circuit syntax regarding your input JSON format.')
ERR_ANGLE = ('Rotation Angle Error',
            'The given angle format or data type in <X> is not correct. It must be a float ' +\
            'number (e.g. 3.14). Please, try again with a correct angle.')
WARN_ORACLE = ('Uncompute Oracle Warning',
              'The given circuit has at least one oracle in it. Since its/their behaviour ' +\
              'cannot be defined, the uncompute pattern will not be analysed.')
WARN_ROTATE = ('Uncompute Rotation Warning',
               'The given circuit has at least one rotation gate in it.Since its/their angle' +\
               ' cannot be coded in the serialization string, the following replacement will ' +\
               'be done:',
               '\n<ul class="light-grey">\n\t<li> Rotation X --> Pauli X</li>\n\t' +\
               '<li> Rotation Y --> Pauli Y</li>\n\t<li> Rotation Z --> Pauli Z</li>\n\t' +\
               '<li> Rotation 1 --> Pauli X</li>\n</ul>')
QPAINTER_URL = 'http://172.20.48.7:8000/'
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

# Create your views here.
def index(request):
    '''Render Home Page appropriatelly'''
    context = {'circuit': '',
               'patterns': get_patterns(),
               'warn_title': ''}

    if request.method == 'POST':
        # 0) Extract info from request
        input_circ = request.POST['input_circ']
        warnings = []
        input_format = 'json'

        # 1) Check empty circuit --> Clear button
        if input_circ == '':
            return render(request, 'index.html', context=context)
        
        if input_circ == '[]' or input_circ == '{}':
            context['err_title'] = ERR_CIRCUIT[0]
            context['err_msg'] = ERR_CIRCUIT[1]
            return render(request, 'index.html', context=context)

        if input_format == 'json':
            # 2) Initial Input Checking
            ## 2.1) Circuit string checking
            try:
                response = requests.get(f'{QPAINTER_URL}check/{input_circ}')
            except Exception:
                context['err_title'] = ERR_CONNECTION[0]
                context['err_msg'] = ERR_CONNECTION[1]
                return render(request, 'index.html', context=context)
            err_info = circuit_ok(response)
            if err_info[0] is not None: # Incorrect Circuit
                context['err_title'] = err_info[0]
                context['err_msg'] = err_info[1]
                context['circuit'] = input_circ
                return render(request, 'index.html', context=context)
            context['circuit'] = input_circ

            ## 2.2) Oracle and rotation checking
            if contain_oracles(eval(input_circ)):
                warnings.append(WARN_ORACLE)

            if contain_rotation(eval(input_circ)):
                warnings.append(WARN_ROTATE)

            if len(warnings) > 0: # At least one warning
                context['warnings'] = warnings

            # 3) Circuit Processing
            # 3.1) SM Processing
            sm_finder = sm.StateMachine()
            if sm_finder.start(input_circ, verbose=False) != 0:
                print('DFA returned an error')
                context['err_title'] = ERR_PROCESSING[0]
                context['err_msg'] = ERR_PROCESSING[1]
                return render(request, 'index.html', context=context)
            sm_matches = sm_finder.found
            front_matches = sm_to_front(sm_matches)

            # 3.2) Simulator Processing
            has_uncompute = sim.main(eval(input_circ))
            if has_uncompute == 1: # Uncompute pattern found
                patt_id = sum(len(matches) for matches in front_matches.values())
                patt_tuple = (0,0,input_circ)
                front_matches['uncompute'] = {patt_id: patt_tuple}
            context['matches'] = front_matches

            # 4) Recommendations and Warnings
            supervisor = sup.Supervisor(has_uncompute,
                                        front_matches[PATTERN_ACHRONYMS['INI']],
                                        sm_finder.non_sup)
            warnings = supervisor.check_all()
            if warnings:
                context['feedback'] = warnings

        return render(request, 'index.html', context=context)

    return render(request, 'index.html', context=context)
