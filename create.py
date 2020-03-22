from application import db
from application.models import Projects, Tasks

db.drop_all()
db.create_all()
