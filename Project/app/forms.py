from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, SelectField, SelectMultipleField, SubmitField 
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import *
from app import db

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

class ActivitiesForm(FlaskForm):
    activityField = SelectMultipleField("Activities", coerce=int)
    submit = SubmitField()
    def __init__(self):
        super(ActivitiesForm, self).__init__()
        options = []
        if Activity is not None:
            for a in Activity.query.all():
                options.append((a.id, a.name))
            self.activityField.choices = options

class ConnectionsForm(FlaskForm):
    closefriends = SelectMultipleField("Close friends",coerce=int)
    classfriends = SelectMultipleField("Friends from lunch or class",coerce=int)
    submit = SubmitField()
    def __init__(self):
        super(ConnectionsForm, self).__init__()
        options = []
        if Activity is not None:
            for s in Students.query.all():
                options.append((s.id, s.firstN + " " + s.lastN))
            self.closefriends.choices = options
            self.classfriends.choices = options
