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
    task = db.relationship('Tasks', backref='task', lazy=True)

    def __repr__(self): 
        return ''.join([
            'Project Name: ', self.project_name, '\r\n', 
            'Project Owner: ', self.owner, '\r\n', 
            'Due Date: ', self.due_date, '\r\n',
            'Start Date: ', self.start_date, '\r\n',
            'End Date: ', self.end_date, '\r\n',
            'Status: ', self.owner, '\r\n'
            ])
################################################################################################            
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(30), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user = db.Column(db.String(50), nullable=False, unique=False)
    due_date = db.Column(db.DateTime, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(10))

    def __repr__(self):
        return ''.join([
            'Task Name: ', self.task_name, '\r\n', 
            'Project Owner: ', self.id, '\r\n', 
            'User: ', self.user, '\r\n',
            'Due Date: ', self.due_date, '\r\n',
            'Start Date: ', self.start_date, '\r\n',
            'End Date: ', self.end_date, '\r\n',
            'Status: ', self.owner, '\r\n'
            ])
################################################################################################            