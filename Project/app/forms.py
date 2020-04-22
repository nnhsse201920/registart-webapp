from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, SelectField, SelectMultipleField, SubmitField 
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import *

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired()])
    lastname = StringField('Last Name',validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Password must be at least 6 characters long.")])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',message="Passwords must match.")])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Organizers.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username in use, please choose a different one.')

    def validate_email(self, email):
        user = Organizers.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address is associated with an existing account.')

class Select2MultipleField(QuerySelectMultipleField):

    def pre_validate(self, form):
        # Prevent "not a valid choice" error
        pass

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = ",".join(valuelist)
        else:
            self.data = ""

def activity_query():
    return Activity.query.filter_by()

class ActivitiesForm(FlaskForm):
    activities = QuerySelectMultipleField("Activities", query_factory=activity_query)
    submit = SubmitField()

class ConnectionsForm(FlaskForm):
    closefriends = Select2MultipleField("Close friends", [],
            choices=[("tc", "Tom Carsello"), ("lz", "Luke Zhang"), ("ehe", "Ethan He"),("jame","James Huang")],
            render_kw={"multiple": "multiple"})
    classfriends = Select2MultipleField("Friends from lunch or class", [],
            choices=[("tc", "Tom Carsello"), ("lz", "Luke Zhang"), ("ehe", "Ethan He"),("jame","James Huang")],
            render_kw={"multiple": "multiple"})
    submit = SubmitField()
