from application import app, db
from flask import render_template, redirect, url_for, request, flash
from application.forms import ProjectForm, EditProjectForm, TaskForm, EditTaskForm
from application.models import Projects, Tasks

###################################################################################
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

###################################################################################
@app.route('/about')
def about():
    return render_template('about.html', title='About')

###################################################################################
@app.route('/projects')
def projects():
	projectData = Projects.query.all()
	return render_template('projects.html', title='Projects', projects=projectData)

###################################################################################
@app.route('/tasks')
def tasks():
	taskData = Tasks.query.all()
	projectData = Projects.query.all()

	return render_template('tasks.html', title='Tasks', tasks=taskData, projects=projectData )

###################################################################################
@app.route('/calender')
def calender():
    return render_template('calender.html', title='Calender')

###################################################################################
@app.route('/board')
def board():
    return render_template('board.html', title='board')

###################################################################################
@app.route('/addproject', methods=['GET', 'POST'])
def addproject():
	#status_types = ['Under Process','Done','For Review','For Approval','On Hold']

	form = ProjectForm()
	if form.validate_on_submit():
		projectData = Projects(
			project_name=form.project_name.data,
			owner=form.owner.data,
			due_date=form.due_date.data,
			start_date=form.start_date.data,
			end_date=form.end_date.data,
			status=form.status.data
			)
		db.session.add(projectData)
		db.session.commit()
		return redirect(url_for('projects'))
	else:
		print(form.errors)

	return render_template('addproject.html', title='Add Project', form=form)
###################################################################################
@app.route('/editproject/<int:id>', methods=['GET', 'POST'])
def editproject(id):
	project=Projects.query.filter_by(id=id)
	projectData = project.first()
	form = EditProjectForm()
	if form.validate_on_submit():
		projectData.project_name = form.project_name.data
		projectData.owner = form.owner.data
		projectData.due_date = form.due_date.data
		projectData.start_date = form.start_date.data
		projectData.end_date = form.end_date.data
		projectData.status = form.status.data

		db.session.commit()
		return redirect(url_for('projects', id=id))
	elif request.method == 'GET':
		form.project_name.data = projectData.project_name
		form.owner.data = projectData.owner
		form.due_date.data = projectData.due_date
		form.start_date.data = projectData.start_date
		form.end_date.data = projectData.end_date
		form.status.data = projectData.status

	return render_template('editproject.html', title='Edit Project', form=form)
###################################################################################
@app.route("/deleteproject/<int:id>", methods=["GET", "POST"])
def deleteproject(id):
	project=Projects.query.filter_by(id=id)
	projectData = project.first()
	tasks = Tasks.query.filter_by(project_id=id)
	for task in tasks:
		db.session.delete(task)

	db.session.delete(projectData)    
	db.session.commit()   	

	return redirect(url_for('projects'))

###################################################################################
@app.route('/addtask/<int:id>', methods=['GET', 'POST'])
def addtask(id):
	
	project=Projects.query.filter_by(id=id)
	projectData = project.first()
	form = TaskForm()				
	form.project_id.data=projectData.project_name

	if form.validate_on_submit():
		taskData = Tasks(
			task_name=form.task_name.data,
			user=form.user.data,
			project_id=id,
			due_date=form.due_date.data,
			start_date=form.start_date.data,
			end_date=form.end_date.data,
			status=form.status.data,
		)
		db.session.add(taskData)
		db.session.commit()
		return redirect(url_for('tasks'))
	else:
		print(form.errors)
	return render_template('addtask.html', title='Add Task', form=form)
   
###################################################################################
@app.route('/edittask/<int:id>', methods=['GET', 'POST'])
def edittask(id):
	task=Tasks.query.filter_by(id=id)
	taskData = task.first()
	form = EditTaskForm()
	if form.validate_on_submit():
		taskData.task_name = form.task_name.data
		taskData.project_id = form.project_id.data
		taskData.user = form.user.data
		taskData.due_date = form.due_date.data
		taskData.start_date = form.start_date.data
		taskData.end_date = form.end_date.data
		taskData.status = form.status.data

		db.session.commit()
		return redirect(url_for('tasks', id=id))
	elif request.method == 'GET':
		form.task_name.data = taskData.task_name
		form.project_id.data = taskData.project_id
		form.user.data = taskData.user
		form.due_date.data = taskData.due_date
		form.start_date.data = taskData.start_date
		form.end_date.data = taskData.end_date
		form.status.data = taskData.status

	return render_template('edittask.html', title='Edit Task', form=form)
###################################################################################
@app.route("/deletetask/<int:id>", methods=["GET", "POST"])
def deletetask(id):    
	task=Tasks.query.filter_by(id=id)
	taskData = task.first()
	db.session.delete(taskData)    
	db.session.commit()
	return redirect(url_for('tasks'))
###################################################################################