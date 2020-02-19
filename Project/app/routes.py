from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, CheckBox, ActivitiesForm
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
        user = User.query.filter_by(username=form.username.data).first()
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
        user = User(firstname=form.firstname.data, lastname=form.lastname.data,username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account successfully created')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
 

@app.route('/survey/about',methods=['GET', 'POST'])
@login_required
def about():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = CheckBox();
    if form.validate():
        return redirect(url_for('activities'))
    else:
        flash('Please complete this step before proceeding.')
    return render_template('about.html', title='About', form=form,isOnSurvey=True)

@app.route('/survey/rules',methods=['GET', 'POST'])
@login_required
def rules():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = CheckBox();
    if form.validate():
        return redirect(url_for('script'))
    else:
        flash('Please complete this step before proceeding.')
    return render_template('rules.html', title='Illinois Registration Rules', form=form,isOnSurvey=True)

@app.route('/survey/script',methods=['GET', 'POST'])
@login_required
def script():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = CheckBox();
    if form.validate():
        return redirect(url_for('targets'))
    else:
        flash('Please complete this step before proceeding.')
    return render_template('script.html', title='Script', form=form,isOnSurvey=True)

@app.route('/survey/targets',methods=['GET', 'POST'])
@login_required
def targets():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = CheckBox();
    if form.validate():
        return redirect(url_for('manager'))
    else:
        flash('Please complete this step before proceeding.')
    return render_template('targets.html', title='Registration Targets', form=form,isOnSurvey=True)

@app.route('/survey/activities',methods=['GET', 'POST'])
@login_required
def activities():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    checkbox = CheckBox()
    form = ActivitiesForm()
    if form.validate_on_submit():
        return redirect(url_for('connections'))
    return render_template('activities.html', title='Your Activities', checkbox=checkbox, form=form,isOnSurvey=True)

@app.route('/survey/manager',methods=['GET', 'POST'])
@login_required
def manager():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = CheckBox();
    if form.validate():
        return redirect(url_for('index'))
    else:
        flash('Please complete this step before proceeding.')
    return render_template('manager.html', title='Target Contact Manager', form=form,isOnSurvey=True)

@app.route('/survey/connections',methods=['GET', 'POST'])
@login_required
def connections():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    check = CheckBox()
    if check.validate():
        return redirect(url_for('rules'))
    else:
        flash('Please complete this step before proceeding.')
    return render_template('connections.html', title='Registart | Connections', isOnSurvey=True,check=check)
