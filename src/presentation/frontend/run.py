from flask import Flask, render_template, request
from app.forms import FormIngestParameters, FormSelectPath
from app.csv_interpreter import getTableContentMetrics, getTableContentPatterns, getTableHeaderMetrics, getTableHeaderPatterns, getStatistics

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

languageApp=None
extensionApp=None

@app.route('/get-terminal-text', methods=["GET"])
def getTerminalText():
    updated_text = "The tool isn't initialized!"

    if languageApp is not None and extensionApp is not None:
        updated_text = "You have selected ", languageApp, " and ", extensionApp

    return updated_text

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
    form = FormIngestParameters(request.form)

    if form.validate_on_submit():
        language = form.language.data
        from_date = form.from_date.data
        to_date = form.to_date.data

        form.language.data=language
        #form.from_date.data=from_date
        #form.to_date.data=to_date
        languageApp=language
    return render_template("index.html", form=form)

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

    return render_template("dataset_analysis.html", data=data, labels=labels, values=values, results_percentage=results_percentage)
    
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
    
    return render_template("circuit.html", form=form,
                           table_header_Patterns=getTableHeaderPatterns(), table_content_Patterns=getTableContentPatterns(path),
                           table_header_Metrics=getTableHeaderMetrics(), table_content_Metrics=getTableContentMetrics(path),
                           get_circuit_link=get_circuit_link)

    #all_paths = "*"
    #return render_template("circuit.html",
    #                       table_header_Patterns=getTableHeaderPatterns(), table_content_Patterns=getTableContentPatterns(all_paths),
    #                       table_header_Metrics=getTableHeaderMetrics(), table_content_Metrics=getTableContentMetrics(all_paths))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Not found..."), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)