from application import app, db
from flask import render_template, redirect, url_for, request
from application.forms import ProjectForm, EditProjectForm, TaskForm, EditTaskForm
from application.models import Projects, Tasks

###################################################################################
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home', posts=postData)

###################################################################################
@app.route('/about')
def about():
    return render_template('about.html', title='about')

###################################################################################
@app.route('/addproject', methods=['GET', 'POST'])
def project():
	form = ProjectForm()
	if form.validate_on_submit():
		projectData = Projects(
			project_name=form.project_name.data,
			owner=form.owner.data,
			due_date=form.due_date.data,
			start_date=form.start_date.data,
			end_date=form.end_date.data,
			status=form.status.data,
		)
		db.session.add(projectData)
		db.session.commit()
		return redirect(url_for('projects'))
	else:
		print(form.errors)
	return render_template('addproject.html', title='Add Project', form=form)

###################################################################################
@app.route('/editproject', methods=['GET', 'POST'])
def editproject():
	form = EditProjectForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('editproject.html', title='Edit Project', form=form)
###################################################################################
@app.route("/account/delete", methods=["GET", "POST"])
def deleteproject():
        user = current_user.id
        posts = Posts.query.filter_by(user_id=user)
        for post in posts:
                db.session.delete(post)
        account = Users.query.filter_by(id=user).first()
        logout_user()
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for('projects'))
###################################################################################
@app.route('/addtask', methods=['GET', 'POST'])
def task():
	form = TaskForm()
	if form.validate_on_submit():
		tasktData = Tasks(
			task_name=form.task_name.data,
			project_id=form.project_id.data,
			user=form.user.data
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
@app.route('/edittask', methods=['GET', 'POST'])
def edittask():
	form = EditTaskForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('edittask.html', title='Edit Task', form=form)
###################################################################################
@app.route("/account/delete", methods=["GET", "POST"])
def deletetask():
        user = current_user.id
        posts = Posts.query.filter_by(user_id=user)
        for post in posts:
                db.session.delete(post)
        account = Users.query.filter_by(id=user).first()
      
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for('tasks'))
###################################################################################