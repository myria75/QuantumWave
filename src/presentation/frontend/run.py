from types import NoneType
from flask import Flask, render_template, request, jsonify, session
from .app.forms import FormIngestParameters, FormSelectPath, FormSelectRepo
from .app.csv_interpreter import getTableContentMetrics, getTableContentPatterns, getTableHeaderMetrics, getTableHeaderPatterns, getStatistics, getMinimum, getMaximun, getAverage, getStandardDeviation
from .app.mongo_handler import getFilesList, getRepositoriesList
import threading
import time
import configparser
import logging

import os
from pymongo import MongoClient, cursor
import json
from . import mainIngestion

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

languageApp=None
extensionApp=None

isIngestionRunning = False
ingestionThread = None
stopThread = False

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))

connection = MongoClient(db_link, socketTimeoutMS=None)
dbGithub = connection[db_name] 
collRepo = dbGithub[db_coll]

defaultProgressJson = {
    "totalRepos_ingest": None,
	"ingestedRepos": None,
	"totalFiles_analysis": None,
	"analyzedFiles": None
}

jsonPath = os.path.join('progress_temp.json')


def executeIngest(languages, from_date, to_date):
    global isIngestionRunning, ingestionThread, stopThread
    try:
        isIngestionRunning = True
        stopThread = False
        while not stopThread:
            mainIngestion.mainIngestion(languages, from_date, to_date)
    finally:
        isIngestionRunning = False

def stopIngestion():
    global isIngestionRunning, stopThread
    stopThread = True
    isIngestionRunning = False

@app.route('/ingest', methods=['GET', 'POST'])
def handle_ingest():
    if request.method == 'POST':
        language = request.form['language']
        print("Language:", language)
        return "Formulario enviado exitosamente" 
    else:
        return render_template("index.html")  # O cualquier otra plantilla que desees mostrar

@app.route('/', methods=["get", "post"])
def home():
    global isIngestionRunning, ingestionThread, languageApp
    form = FormIngestParameters(request.form)

    if form.validate_on_submit():
        language = form.language.data
        from_date = form.from_date.data
        to_date = form.to_date.data

        form.language.data=language
        #form.from_date.data=from_date
        #form.to_date.data=to_date
        languageApp=language

        if not isIngestionRunning:
            stopIngestion()
            ingestionThread = threading.Thread(target=executeIngest, name="MainIngestQuanticWave", args=(language, from_date, to_date))
            ingestionThread.start()
        #return jsonify({'status': 'Thread started'}), 200
    else:
        isIngestionRunning = False
    return render_template("index.html", form=form)

@app.route('/cancel-ingest', methods=['POST'])
def cancelIngest():
    stopIngestion()
    return 'Función ejecutada exitosamente'

@app.route('/dataset_analysis', methods=['GET', 'POST'])
def dataset_analysis():
    pattern_statistics = getStatistics()

    data = [
        ("Initialization", pattern_statistics[0]),
        ("Superposition", pattern_statistics[1]),
        ("Oracle", pattern_statistics[2]),
        ("Entanglement", pattern_statistics[3]),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    results_percentage = []
    
    for statistic in pattern_statistics: 
        percentage = round((statistic/612)* 100, 2)
        results_percentage.append(percentage)

    table_header_Metrics=getTableHeaderMetrics()
    table_header_Metrics[0] = "Metrics"

    popover_contents = [
        "This table shows all metric grouped according to mean, standard deviation, minimum and maximum.",
        "Number of qubits in the circuit",
        "Maximum number of operations in a cubit",
        "Maximum number of simultaneous trasactions",
        "Average number of simultaneous transactions",
        "Pauli-X assumes a rotation of π radians around the X axis of the Bloch sphere. This gate belogns to the group of quantum gates that apply to a single qubit",
        "Pauli-Y assumes a rotation of π radians around the Y axis of the Bloch sphere. This gate belongs to the group of quantum gates that apply to a single qubit",
        "Pauli-Z assumes a rotation of π radians aound the Z axis of the Bloch sphere. This gate belongs to the group of quantum gates that apply to a single qubit",
        "Pauli gates assume a rotation of pi radians around the X, Y and Z axes of the Bloch sphere. These gates belong to the group of quantum gates that apply to a single gates",
        "Hadamard belongs to the group of quantum gates that apply to a single qubit",
        "Superposition means that a qubit can be represented by both 0 and 1 at the same time",
        "Simple gates include identity, Pauli, Hadamard, phase shift, rotation and mesurement gates",
        "Simple gates include identity, Pauli, Hadamard, phase shift, rotation and mesurement gates",
        "Controlled gates belong to the group of quantum gates that apply to several qubits",
        "SWAP gate exchanges the values of two qubits. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "Number of quantum gates, irrespective of type",
        "These gates belong to multi-qubit quantum gates",
        "Presence of single qubit gates int the circuit",
        "Reuses a calculation from a quantum algorithm",
        "The controlled gates of the simple quantum gates group are combined with the oracle algorithm",
        "Presence of oracles in the circuit",
        "Presence of qubits that are affected by controlled oracles",
        "Its application causes the qubit to collapse in its current state, its effect is not reversible",
        "Its application causes the qubit to collapse in its current state, its effect is not reversible",
        "Its application causes the qubit to collapse in its current state, its effect is not reversible",
        "Presence of measured qubits in the circuit"
    ]

    header_popover = list(zip(table_header_Metrics, popover_contents))

    return render_template("dataset_analysis.html", data=data, labels=labels, values=values, results_percentage=results_percentage,
        table_header_Metrics=table_header_Metrics, header_popover = header_popover, table_average=getAverage(), table_standard_desviation=getStandardDeviation(), table_minimun=getMinimum(), table_maximun=getMaximun())
    
def get_circuit_link(circuit):
    return "http://172.20.48.7:8000/"+circuit+"/"

@app.route('/circuit', methods=['GET', 'POST'])
def circuit():
    formRepo = FormSelectRepo(request.form)
    formPath = FormSelectPath(request.form)

    if 'path' in session:
        print(f"TENGO SESION 1 {session['path']}")

    if formRepo.validate_on_submit():
        session['repository'] = formRepo.repositories.data
        formPath.path.choices = []
        for item in getFilesList(session['repository']):
            formPath.path.choices.append((item,item))
        session['repository'] = formRepo.repositories.data
        
        session['path_choices'] = formPath.path.choices
        session['path'] = formPath.path.choices[0][0]
        formPath.path.data = formPath.path.choices[0][0]

        if 'path' in session:
            print(f"TENGO SESION 2 {session['path']}")

    if formPath.validate_on_submit():
        print("PUES ME HE ACTUALIZADO")
        session['path'] = formPath.path.data

        if 'path' in session:
            print(f"TENGO SESION 3 {session['path']}")

    if 'repository' in session:
        formRepo.repositories.data = session['repository']

    codeDoc = {
        "content": ""
    }
    
    if 'path_choices' in session:
        formPath.path.choices = session['path_choices']

    if 'path' in session:
        formPath.path.data = session['path']

        if 'path' in session:
            print(f"TENGO SESION 4 {session['path']}")

        query = {
            "path":"{}".format(formPath.path.data)
        }
        codeDoc: cursor.Cursor = collRepo.find_one(query, no_cursor_timeout=True)
       

        
    
    #formRepo.repositories.data = repository
    #formPath.path.data = path

    table_header_Metrics=getTableHeaderMetrics()
    popover_contents = [
        "This table shows all metric grouped according the ingested circuits.",
        "Number of qubits in the circuit",
        "Maximum number of operations in a qubit",
        "Maximum number of simultaneous trasactions",
        "Average number of simultaneous transactions",
        "Pauli-X assumes a rotation of π radians around the X axis of the Bloch sphere. This gate belogns to the group of quantum gates that apply to a single qubit",
        "Pauli-Y assumes a rotation of π radians around the Y axis of the Bloch sphere. This gate belongs to the group of quantum gates that apply to a single qubit",
        "Pauli-Z assumes a rotation of π radians aound the Z axis of the Bloch sphere. This gate belongs to the group of quantum gates that apply to a single qubit",
        "Pauli gates assume a rotation of pi radians around the X, Y and Z axes of the Bloch sphere. These gates belong to the group of quantum gates that apply to a single gates",
        "Hadamard belongs to the group of quantum gates that apply to a single qubit",
        "Superposition means that a qubit can be represented by both 0 and 1 at the same time",
        "Simple gates include identity, Pauli, Hadamard, phase shift, rotation and mesurement gates",
        "Simple gates include identity, Pauli, Hadamard, phase shift, rotation and mesurement gates",
        "Controlled gates belong to the group of quantum gates that apply to several qubits",
        "SWAP gate exchanges the values of two qubits. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "At least one of the qubits is used as a control element in the operation. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "It is evaluated whether the two controls are in the state |1⟩, while a controlled gate is applied to the remaining qubit. It belongs to multi-qubit quantum gates",
        "Number of quantum gates, irrespective of type",
        "These gates belong to multi-qubit quantum gates",
        "Presence of single qubit gates int the circuit",
        "Reuses a calculation from a quantum algorithm",
        "The controlled gates of the simple quantum gates group are combined with the oracle algorithm",
        "Presence of oracles in the circuit",
        "Presence of qubits that are affected by controlled oracles",
        "Its application causes the qubit to collapse in its current state, its effect is not reversible",
        "Its application causes the qubit to collapse in its current state, its effect is not reversible",
        "Its application causes the qubit to collapse in its current state, its effect is not reversible",
        "Presence of measured qubits in the circuit"
    ]

    header_popover = list(zip(table_header_Metrics, popover_contents))
    
    return render_template("circuit.html", formPath=formPath, formRepo=formRepo, header_popover = header_popover,
                           table_header_Patterns=getTableHeaderPatterns(), table_content_Patterns=getTableContentPatterns(formPath.path.data),
                           table_header_Metrics=getTableHeaderMetrics(), table_content_Metrics=getTableContentMetrics(formPath.path.data),
                           get_circuit_link=get_circuit_link, code_path=formPath.path.data, code_content=codeDoc["content"])

    #all_paths = "*"
    #return render_template("circuit.html",
    #                       table_header_Patterns=getTableHeaderPatterns(), table_content_Patterns=getTableContentPatterns(all_paths),
    #                       table_header_Metrics=getTableHeaderMetrics(), table_content_Metrics=getTableContentMetrics(all_paths))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Not found..."), 404

@app.route('/ingest-status', methods=['GET'])
def thread_status():
    global isIngestionRunning
    percentage_progress = 0

    updated_text = "The tool isn't initialized!"
    mainIngestion.log_capture_string.flush()
    updated_text = mainIngestion.log_capture_string.getvalue()

    if languageApp is not None and extensionApp is not None:
        updated_text = "You have selected ", languageApp, " and ", extensionApp

    if not isIngestionRunning:
        percentage_progress = 0
    else:
        firstHalf_percentage = 0
        secondHalf_percentage = 0

        jsonProgress = {}

        with open(jsonPath, 'r') as file:
            jsonProgress = json.load(file)

        if jsonProgress['totalRepos_ingest'] is not None and jsonProgress['ingestedRepos'] is not None:
            firstHalf_percentage = jsonProgress['ingestedRepos']/jsonProgress['totalRepos_ingest']
            if firstHalf_percentage > 1:
                firstHalf_percentage = 1
            firstHalf_percentage = round(firstHalf_percentage, 2)
            firstHalf_percentage = firstHalf_percentage*100
            
            if jsonProgress['totalFiles_analysis'] is not None and jsonProgress['analyzedFiles'] is not None:
                secondHalf_percentage = jsonProgress['analyzedFiles']/jsonProgress['totalFiles_analysis']
                if secondHalf_percentage > 1:
                    secondHalf_percentage = 1
                secondHalf_percentage = round(secondHalf_percentage, 2)
                secondHalf_percentage = secondHalf_percentage*100
        
        percentage_progress = firstHalf_percentage+secondHalf_percentage

    if percentage_progress > 100:
        percentage_progress = 100
    if percentage_progress < 0:
        percentage_progress = 0

    return jsonify({
        'thread_running': isIngestionRunning,
        'terminal_text': updated_text,
        'percentage_progress_bar': percentage_progress
    }), 200

def runFrontend(host='0.0.0.0', port=5000, debug=False):
    with open(jsonPath, 'w') as file:
        json.dump(defaultProgressJson, file, indent=4)
    try:
        app.run(host=host, port=port, debug=debug)
    finally:
        stopIngestion()

if __name__ == "__main__":
    runFrontend(host='0.0.0.0', port=5000, debug=True)