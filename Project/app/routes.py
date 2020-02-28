from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import *
from app.models import *


@app.route('/')
@app.route('/index')
@login_required
def index():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    return render_template('index.html',current_user=current_user,isOnSurvey=False)

@app.route('/survey')
def survey():
    return render_template('survey.html', title='Survey')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('about'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Organizers.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('about')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('about'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Organizers(firstN=form.firstname.data, lastN=form.lastname.data,username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('about'))
    return render_template('register.html', title='Register', form=form)
 

@app.route('/survey/about',methods=['GET', 'POST'])
@login_required
def about():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    flash('Please complete this step before proceeding.')
    return render_template('about.html', title='About', isOnSurvey=True)

@app.route('/survey/activities',methods=['GET', 'POST'])
@login_required
def activities():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = ActivitiesForm()
    if form.validate_on_submit():
        return redirect(url_for('connections'))
    flash('Please complete this step before proceeding.')
    return render_template('activities.html', title='Your Activities', form=form,isOnSurvey=True)

@app.route('/survey/connections',methods=['GET', 'POST'])
@login_required
def connections():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = ConnectionsForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    flash('Please complete this step before proceeding.')
    return render_template('connections.html', title='Registart | Connections', isOnSurvey=True)
