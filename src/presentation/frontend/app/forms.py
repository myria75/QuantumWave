from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SelectMultipleField, ValidationError
from wtforms.fields.datetime import DateField
from wtforms.validators import InputRequired
from wtforms.widgets import ListWidget, CheckboxInput


from .csv_interpreter import getAllPaths
from .mongo_handler import getRepositoriesList, getFilesList

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

def at_least_one_checkbox(form, field):
    if not field.data:
        raise ValidationError('At least one option must be selected.')

class FormIngestParameters(FlaskForm):
    language = MultiCheckboxField("Language", validators=[at_least_one_checkbox], choices=[("Qiskit", "Qiskit"), ("OpenQASM", "OpenQASM")])
    from_date = DateField("From")#, format='%d/%m/%Y')
    to_date = DateField("To")#, format='%d/%m/%Y')
    start = SubmitField('Start')
    cancel = SubmitField('Cancel')


class FormSelectRepo(FlaskForm):
    choices = []

    for item in getRepositoriesList():
        choices.append((item,item))

    repositories = SelectField("Repositories", validators=[InputRequired("This field is required")], choices=choices)

class FormSelectPath(FlaskForm):
    choices = []
    path = SelectField("Path", validators=[InputRequired("This field is required")], choices=choices)
