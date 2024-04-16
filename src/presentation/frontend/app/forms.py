from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.validators import InputRequired

class FormIngestParameters(FlaskForm):
    language = SelectField("Language", validators=[InputRequired("This field is required")], choices=[("Python", "Python"), ("OpenQASM", "OpenQASM")])
    extension = SelectField("Extension", validators=[InputRequired("This field is required")], choices=[("Cirq", "Cirq"), ("Qiskit", "Qiskit")])
    from_date = DateField("From", format='%d/%m/%Y')
    to_date = DateField("To", format='%d/%m/%Y')
    ingest = SubmitField('Ingest')