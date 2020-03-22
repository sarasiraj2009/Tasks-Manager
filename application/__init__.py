from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from os import getenv

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes