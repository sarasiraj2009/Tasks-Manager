from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.models import Projects, Tasks

class ProjectForm(FlaskForm):
    status_types = [('Under Process','Under Process'),
                    ('Done','Done'),
                    ('For Review','For Review'),
                    ('For Approval','For Approval'),
                    ('On Hold','On Hold')]

    project_name = StringField('Project Name', validators = [DataRequired(), Length(min=5, max=100)])
    owner = StringField('Project Owner', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', validators = [Length(min=2, max=50)])
    status = SelectField(label='Status', choices=status_types)

    submit = SubmitField('Add Project')

#########################################################################################################
class EditProjectForm(FlaskForm):
    status_types = [('Under Process','Under Process'),
                    ('Done','Done'),
                    ('For Review','For Review'),
                    ('For Approval','For Approval'),
                    ('On Hold','On Hold')]

    project_name = StringField('Project Name', validators = [DataRequired()])
    owner = StringField('Project Owner', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', format='%d-%m-%Y', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', format='%d-%m-%Y', validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', format='%d-%m-%Y', validators = [Length(min=2, max=50)])
    status = SelectField(label='Status', choices=status_types)

    submit = SubmitField('Edit Project')
#########################################################################################################

class TaskForm(FlaskForm):
    status_types = [('Under Process','Under Process'),
                    ('Done','Done'),
                    ('For Review','For Review'),
                    ('For Approval','For Approval'),
                    ('On Hold','On Hold')]
    
   
    task_name = StringField('Task Name', validators = [DataRequired(), Length(min=5, max=100)])
    project_id = StringField('Project', validators = [DataRequired()])
    user = StringField('User', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', format='%d-%m-%Y', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', format='%d-%m-%Y',validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', format='%d-%m-%Y', validators = [Length(min=2, max=50)])
    status = SelectField(label='Status', choices=status_types)

    submit = SubmitField('Add Task')

#########################################################################################################

class EditTaskForm(FlaskForm):
    status_types = [('Under Process','Under Process'),
                    ('Done','Done'),
                    ('For Review','For Review'),
                    ('For Approval','For Approval'),
                    ('On Hold','On Hold')]

    task_name = StringField('Task Name', validators = [DataRequired(), Length(min=5, max=100)])
    project_id = StringField('Project', validators = [DataRequired()])
    user = StringField('User', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', validators = [Length(min=2, max=50)])
    status = SelectField(label='Status', choices=status_types)

    submit = SubmitField('Edit Task')
#########################################################################################################