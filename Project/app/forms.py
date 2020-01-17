from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms.validators import DataRequired

class CheckBox(FlaskForm):
    check = BooleanField('I have completed this step', validators=[DataRequired()])