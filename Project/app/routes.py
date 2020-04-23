from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import *
from app.models import *
import pymysql

dbConnect = pymysql.connect("localhost", "registart", "database7", "registart")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='About', current_user=current_user)

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
    return redirect(url_for('index'))

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
    return render_template('register.html', title='Get Started', form=form)


@app.route('/survey/activities',methods=['GET', 'POST'])
@login_required
def activities():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = ActivitiesForm()
    user = Organizers.query.filter_by(username=current_user.username).first()
    if form.validate_on_submit():
        userActivities = form.activityField.data # the IDs of activities that the user selected
        print(userActivities)
        for i in range(len(userActivities)):
            for activity in Activity.query.all():
                if userActivities[i] == activity.id:
                    activity = Activity.query.filter_by(id=activity.id).first()
                    activity.members.append(user) 
        db.session.commit()
        return redirect(url_for('relationships'))
    return render_template('activities.html', title='Your Activities', form=form)

@app.route('/survey/connections',methods=['GET', 'POST'])
@login_required
def connections():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = ConnectionsForm()
    if form.validate_on_submit():
        return redirect(url_for('relationships'))
    flash('Please complete this step before proceeding.')
    return render_template('connections.html', title='Connections', isOnSurvey=True,form=form)


@app.route('/survey/relationships', methods=['GET', 'POST'])
@login_required
def relationships():
    if current_user.is_anonymous:
        return redirect(url_for('index'))
    flash('Please complete this step before proceeding.')
    cursor = dbConnect.cursor()
    cursor.execute("SELECT CONCAT(firstN, ' ', lastN) as fullName FROM students ORDER BY firstN")
    stuNames = cursor.fetchall()
    stuNames = [i[0] for i in stuNames]
    return render_template('relationships.html', title='Relationships', isOnSurvey=True, stuNames=stuNames)

