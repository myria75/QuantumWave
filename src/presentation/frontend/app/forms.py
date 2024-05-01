from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.validators import InputRequired

from .csv_interpreter import getAllPaths

class FormIngestParameters(FlaskForm):
    language = SelectField("Language", validators=[InputRequired("This field is required")], choices=[("Default", "Select"), ("Qiskit", "Qiskit"), ("OpenQASM", "OpenQASM")])
    from_date = DateField("From", format='%d/%m/%Y')
    to_date = DateField("To", format='%d/%m/%Y')
    ingest = SubmitField('Ingest')

class FormSelectPath(FlaskForm):
    choices = []

    for item in getAllPaths():
        choices.append((item,item))

    path = SelectField("Path", validators=[InputRequired("This field is required")], choices=choices)