from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User

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
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username in use, please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address is associated with an existing account.')
            
class CheckBox(FlaskForm):
    check = BooleanField('I have completed this step', validators=[DataRequired()])

class ActivitiesForm(FlaskForm):
    activity1 = StringField('Activity 1')
    activity2 = StringField('Activity 2')
    activity3 = StringField('Activity 3')
    activity4 = StringField('Activity 4')
    activity5 = StringField('Activity 5')
    activity6 = StringField('Activity 6')
    activity7 = StringField('Activity 7')
    activity8 = StringField('Activity 8')
    submit = SubmitField('Sign In')
    check = BooleanField('I have completed this step', validators=[DataRequired()])
