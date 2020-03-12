from application import db
from datetime import datetime


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False, unique=True)
    owner = db.Column(db.String(50), nullable=False, unique=False)
    due_date = db.Column(db.DateTime, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(10))

    #def __repr__(self):
    #    return ''.join([
    #        'Project ID: ', self.projectid, '\r\n',
    #        'Title: ', self.title, '\r\n', self.content
    #    ])


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Tasks_name = db.Column(db.String(30), nullable=False)
    Project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user = db.Column(db.String(50), nullable=False, unique=False)
    due_date = db.Column(db.DateTime, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(10))

   
    post = db.relationship('Projects', backref='author', lazy=True)

    #def __repr__(self):
    #    return ''.join(['UserID: ', str(self.id), '\r\n',
    #    'Email: ', self.email], '\r\n',
    #    'Name: ', self.first_name, ' ', self.last_name