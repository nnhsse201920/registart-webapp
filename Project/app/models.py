from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

participants = db.Table('participants',
    db.Column('organizer_id',db.Integer,db.ForeignKey('organizers.id'), primary_key=True),
    db.Column('activity_id',db.Integer,db.ForeignKey('activity.id'), primary_key=True)
    )

class Organizers(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstN = db.Column(db.VARCHAR(255), index=True)
    lastN = db.Column(db.VARCHAR(255), index=True)
    username = db.Column(db.VARCHAR(255), index=True, unique=True)
    organizationID = db.Column(db.Integer(), index=True)
    email = db.Column(db.VARCHAR(255), index=True, unique=True)
    password = db.Column(db.VARCHAR(255), index=True)

    activities = db.relationship('Activity', secondary=participants, backref=db.backref('members', lazy='dynamic'))
    
    #relationships = db.relationship('Connection',secondary=connections, backref=db.backref('known',lazy='dynamic'))

    def __repr__(self):
        return '<Organizer> {}'.format(self.username)
    def set_password(self, p):
        self.password = generate_password_hash(p)
    def check_password(self, p):
        return check_password_hash(self.password, p)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64), unique=True)

    def __str__(self):
        return self.name
    def __repr__(self):
        return '<Activity> {}'.format(self.name)
    
class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64), unique=True)
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return '<Activity> {}'.format(self.name)

class Assignments(db.Model):
    organizerID = db.Column(db.Integer(), primary_key=True)
    studentID = db.Column(db.Integer(), index=True, unique=True)
    lastContact = db.Column(db.DateTime, index=True, unique=True)
    status = db.Column(db.Integer(), index=True, unique=True)
    medium = db.Column(db.Integer(), index=True, unique=True)      
                               
class Organizations(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.VARCHAR(255), index=True, unique=True)

class Students(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstN = db.Column(db.VARCHAR(255), index=True, unique=True)
    lastN = db.Column(db.VARCHAR(255), index=True, unique=True)
    targetID = db.Column(db.VARBINARY(255), index=True, unique=True)
    organizationID = db.Column(db.Integer(), index=True, unique=True)
    isOrganizer = db.Column(db.SmallInteger(), index=True, unique=True)          

@login.user_loader
def load_user(id):
    return Organizers.query.get(int(id))
