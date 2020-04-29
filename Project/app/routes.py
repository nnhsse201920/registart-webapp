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
    user = Organizers.query.filter_by(username=current_user.username).first()
    user.activities.clear()
    db.session.commit()
    form = ActivitiesForm()
    if form.validate_on_submit():
        userActivities = form.activityField.data # list of IDs of the activities that the user selected
        for i in userActivities:
            for a in Activity.query.all():
                if i == a.id:
                    activity = Activity.query.filter_by(id=a.id).first()
                    activity.members.append(user) 
        db.session.commit()
        return redirect(url_for('relationships'))
    return render_template('activities.html', title='Your Activities', form=form)

@app.route('/survey/connections', methods=['GET', 'POST'])
@login_required
def connections():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = ConnectionsForm()
    if form.validate_on_submit():
        return redirect(url_for('relationships'))
    return render_template('connections.html', title='Connections', isOnSurvey=True,form=form)

@app.route('/survey/relationships', methods=['GET', 'POST'])
@login_required
def relationships():
    if current_user.is_anonymous:
        return redirect(url_for('index'))
    cursor = dbConnect.cursor()
    cursor.execute("SELECT CONCAT(firstN, ' ', lastN) as fullName FROM students ORDER BY firstN")
    stuNames = cursor.fetchall()
    stuNames = [i[0] for i in stuNames]
    user = Organizers.query.filter_by(username=current_user.username).first()
    return render_template('relationships.html', title='Relationships', isOnSurvey=True, stuNames=stuNames)

@app.route('/survey/rankings', methods=['GET','POST'])
@login_required
def rankings():
    if current_user.is_anonymous:
        return redirect(url_for('index'))
    students = []
    user = Organizers.query.filter_by(username=current_user.username).first()
    userRelationships = user.relationships
    for u in userRelationships:
        students.append(u.firstN + " " + u.lastN)
    return render_template('rankings.html', title = 'Rankings', isOnSurvey=True, students=students)

@app.route('/studentrankings', methods=['GET','POST'])
def studentrankings():
    user = Organizers.query.filter_by(username=current_user.username).first()
    if request.method == "POST":
        relations = user.relationships
        name = request.data.decode("utf-8").split()
        for i in relations:
            if name[0] == i.firstN and name[1] == i.lastN:
                if name[len(name)-1] == "1":
                    i.ranking = 1
                elif name[len(name)-1] == "2":
                    i.ranking = 2
                elif name[len(name)-1] == "3":
                    i.ranking = 3
                else:
                    i.ranking = 4
        db.session.commit()
    return ""

@app.route('/students',  methods=['GET', 'POST'])
def students():
    user = Organizers.query.filter_by(username=current_user.username).first()
    if request.method == "POST":
        name = request.data.decode("utf-8").split()
        if name[len(name)-1] == "1":
            for s in Students.query.all():
                if s.firstN == name[0] and s.lastN == name[1]:
                    namePresent = False
                    for u in user.relationships:
                        if s.firstN == u.firstN and s.lastN == u.lastN:
                            namePresent = True
                    if namePresent == False:
                        student = Connection(firstN=s.firstN,lastN=s.lastN)
                        user.relationships.append(student)
                    db.session.commit()   
        elif name[len(name)-1] == "0":
            for s in Students.query.all():
                if s.firstN == name[0] and s.lastN == name[1]:
                    for u in user.relationships:
                        if s.firstN == u.firstN and s.lastN == u.lastN:
                            student = Connection.query.filter_by(firstN=s.firstN,lastN=s.lastN,user_id=user.id).first()   
                            user.relationships.remove(student)
                            db.session.delete(student)
                    db.session.commit()         
    return ""

@app.route('/survey/end', methods=['GET', 'POST'])
@login_required
def mobile():
    if current_user.is_anonymous:
        return redirect(url_for('index'))
    return render_template('mobile.html', title="Survey Complete", isOnSurvey=True)
    
