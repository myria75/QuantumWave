from flask import Flask, render_template, request
from app.forms import FormIngestParameters, FormSelectPath
from app.csv_interpreter import getTableContentMetrics, getTableContentPatterns, getTableHeaderMetrics, getTableHeaderPatterns

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
        extension = request.form['extension']
        print("Language:", language)
        print("Extension:", extension)
        return "Formulario enviado exitosamente" 
    else:
        return render_template("index.html")  # O cualquier otra plantilla que desees mostrar

@app.route('/', methods=["get", "post"])
def home():
    form = FormIngestParameters(request.form)

    if form.validate_on_submit():
        language = form.language.data
        extension = form.extension.data
        from_date = form.from_date.data
        to_date = form.to_date.data

        form.language.data=language
        form.extension.data=extension
        #form.from_date.data=from_date
        #form.to_date.data=to_date
        languageApp=language
        extensionApp=extension
    return render_template("index.html", form=form)

@app.route('/dataset_analysis', methods=['GET', 'POST'])
def dataset_analysis():
    form = FormSelectPath(request.form)

    data = [
        ("Initialization", 12),
        ("Superposition", 52),
        ("Oracle", 32),
        ("Entanglement", 0),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    path = ""

    if form.validate_on_submit():
        path = form.path.data
        print(path)
    else:
        path = "Python_qiskit_qiskit-community_qiskit-algorithms_test.test_grover.py" #TODO: get first or display none
    form.path.data = path
    return render_template("dataset_analysis.html", form=form, labels=labels, values=values, table_header_Metrics=getTableHeaderMetrics(), table_content_Metrics=getTableContentMetrics(path))
    return render_template("dataset_analysis.html", form=form, labels=labels, values=values, table_header_Patterns=getTableHeaderPatterns(), table_content_Patterns=getTableContentPatterns(path))

@app.route('/circuit')
def circuit():
    return render_template("circuit.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)