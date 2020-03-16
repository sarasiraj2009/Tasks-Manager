# import render_template function from the flask module
from flask import render_template, url_for

# import the app object from the ./application/__init__.py
from application import app

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

# define routes for /projects, this function will be called when these are accessed
@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

# define routes for /tasks, this function will be called when these are accessed
@app.route('/tasks')
def tasks():
    return render_template('tasks.html', title='Tasks')

# define routes for /calender, this function will be called when these are accessed
@app.route('/calender')
def calender():
    return render_template('calender.html', title='Calender')

# define routes for /board, this function will be called when these are accessed
@app.route('/board')
def board():
    return render_template('board.html', title='Board')

# define routes for /about, this function will be called when these are accessed
@app.route('/about')
def about():
    return render_template('about.html', title='About')


