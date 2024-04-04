from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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