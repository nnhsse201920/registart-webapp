from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Organizers(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstN = db.Column(db.VARCHAR(255), index=True, unique=True)
    lastN = db.Column(db.VARCHAR(255), index=True, unique=True)
    username = db.Column(db.VARCHAR(255), index=True, unique=True)
    organizationID = db.Column(db.Integer(), index=True, unique=True)
    email = db.Column(db.VARCHAR(255), index=True, unique=True)
    password = db.Column(db.VARCHAR(255), index=True, unique=True)
    
    def __repr__(self):
        return '<Organizer {}>'.format(self.username)
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)

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
                               
