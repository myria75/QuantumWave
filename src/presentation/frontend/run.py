from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dataset_analysis')
def dataset_analysis():
    return render_template("dataset_analysis.html")

@app.route('/circuit')
def circuit():
    return render_template("circuit.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
