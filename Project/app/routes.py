from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/survey')
def survey():
    return render_template('survey.html', title='Survey')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():

    return render_template('register.html',title='Create Account')