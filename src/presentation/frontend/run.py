from flask import Flask, render_template, request, jsonify
from .app.forms import FormIngestParameters, FormSelectPath
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
        percentage = round((statistic/537)* 100, 2)
        results_percentage.append(percentage)

    table_header_Metrics=getTableHeaderMetrics()
    table_header_Metrics[0] = "Metrics"

    return render_template("dataset_analysis.html", data=data, labels=labels, values=values, results_percentage=results_percentage,
        table_header_Metrics=table_header_Metrics, table_average=getAverage(), table_standard_desviation=getStandardDeviation(), table_minimun=getMinimum(), table_maximun=getMaximun())
    
def get_circuit_link(circuit):
    return "http://172.20.48.7:8000/"+circuit+"/"

@app.route('/circuit', methods=['GET', 'POST'])
def circuit():
    path = ""
    form = FormSelectPath(request.form)

    if form.validate_on_submit():
        path = form.path.data
        print(path)
    else:
        path = "Python_qiskit_qiskit-community_qiskit-algorithms_test.test_grover.py" #TODO: get first or display none
    
    form.path.data = path

    query = {
        "path":"{}".format(path)
    }

    codeDoc: cursor.Cursor = collRepo.find_one(query, no_cursor_timeout=True)
    
    return render_template("circuit.html", form=form,
                           table_header_Patterns=getTableHeaderPatterns(), table_content_Patterns=getTableContentPatterns(path),
                           table_header_Metrics=getTableHeaderMetrics(), table_content_Metrics=getTableContentMetrics(path),
                           get_circuit_link=get_circuit_link, code_path=path, code_content=codeDoc["content"])

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