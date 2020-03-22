from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.models import Projects, Tasks

class ProjectForm(FlaskForm):
    #status_types = ['Under Process','Done','For Review','For Approval','On Hold']

    project_name = StringField('Project Name', validators = [DataRequired(), Length(min=5, max=100)])
    owner = StringField('Project Owner', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', validators = [Length(min=2, max=50)])
    status = StringField('Status')

    submit = SubmitField('Add Project')

#########################################################################################################
class EditProjectForm(FlaskForm):
    #status_types = ['Under Process','Done','For Review','For Approval','On Hold']

    project_name = StringField('Project Name', validators = [DataRequired(), Length(min=5, max=100)])
    owner = StringField('Project Owner', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', validators = [Length(min=2, max=50)])
    status = StringField('Status')

    submit = SubmitField('Edit Project')
#########################################################################################################

class TaskForm(FlaskForm):
    #status_types = ['Under Process','Done','For Review','For Approval','On Hold']

    task_name = StringField('Task Name', validators = [DataRequired(), Length(min=5, max=100)])
    project_id = StringField('Project', validators = [DataRequired(),Length(min=2, max=50)])
    user = StringField('User', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', validators = [Length(min=2, max=50)])
    status = StringField('Status')

    submit = SubmitField('Add Task')

#########################################################################################################

class EditTaskForm(FlaskForm):
    #status_types = ['Under Process','Done','For Review','For Approval','On Hold']

    task_name = StringField('Task Name', validators = [DataRequired(), Length(min=5, max=100)])
    project_id = StringField('Project', validators = [DataRequired(), Length(min=2, max=50)])
    User = StringField('User', validators = [DataRequired(), Length(min=2, max=50)])
    due_date = StringField('Due date', validators = [Length(min=2, max=50)])
    start_date = StringField('Start Date', validators = [Length(min=2, max=50)])
    end_date = StringField('End Date', validators = [Length(min=2, max=50)])
    status = StringField('Status')

    submit = SubmitField('Edit Task')
#########################################################################################################