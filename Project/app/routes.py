from app import app
from flask import render_template

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

@app.route('/survey/about')
def about():
    return render_template('about.html', title='About')