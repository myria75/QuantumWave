from flask import Flask, render_template, request
from app.forms import FormIngestParameters

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

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
        #procesar
    else:
        return render_template("index.html", form=form)

@app.route('/dataset_analysis')
def dataset_analysis():
    data = [
        ("01-01-2020", 1597),
        ("02-01-2020", 1456)
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("dataset_analysis.html", labels=labels, values=values)

@app.route('/circuit')
def circuit():
    return render_template("circuit.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
