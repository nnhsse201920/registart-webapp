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
    return render_template('index.html',current_user=current_user)

@app.route('/survey')
def survey():
    return render_template('survey.html', title='Survey')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Organizers.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('about'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Organizers(firstN=form.firstname.data, lastN=form.lastname.data,username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
 

@app.route('/survey/activities',methods=['GET', 'POST'])
@login_required
def activities():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = ActivitiesForm()
    if form.validate_on_submit():
        return redirect(url_for('connections'))
    return render_template('activities.html', title='Your Activities', form=form)

@app.route('/survey/connections',methods=['GET', 'POST'])
@login_required
def connections():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = ConnectionsForm()
    
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('connections.html', title='Registart | Connections',form=form)

@app.route('/about',methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='Registart | About')
