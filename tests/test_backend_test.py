import unittest

from flask import url_for
from flask_testing import TestCase
import os
from application import app, db
from application.models import Projects, Tasks


class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:sweet3girls@34.89.105.219/test_database')

        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
       
        project = Projects( project_name="Testing", 
                            owner="Admin", 
                            due_date="2020-03-24", 
                            start_date="2020-02-17",
                            end_date="2020-03-23",
                            status="Done")

        task = Tasks(   task_name="Phase 1",
                        project_id=1,
                        user="Admin", 
                        due_date="2020-03-24", 
                        start_date="2020-02-17",
                        end_date="2020-03-23",
                        status="Done")

        db.session.add(project)
        db.session.add(task)

        project = Projects( project_name="Coding", 
                            owner="Admin", 
                            due_date="2020-03-24", 
                            start_date="2020-02-17",
                            end_date="2020-03-23",
                            status="Done")

        task = Tasks(   task_name="Phase 2", 
                        project_id=2,
                        user="Admin", 
                        due_date="2020-03-24",
                        start_date="2020-02-17",
                        end_date="2020-03-23",
                        status="Done")

        db.session.add(project)
        db.session.add(task)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestModels(TestBase):
    def test_projects_model(self):
        self.assertEqual(Projects.query.count(), 2)

        project = Projects.query.filter_by(id=1).first()
        self.assertEqual(project.project_name, 'Testing')
        self.assertEqual(project.owner, 'Admin')

    def test_tasks_model(self):
        self.assertEqual(Tasks.query.count(), 2)

        task = Tasks.query.filter_by(id=1).first()
        self.assertEqual(task.task_name, 'Phase 1')

   
class TestUpdate(TestBase):

    def test_update_project(self):
        project = Projects.query.filter_by(id=2).first()

        project.project_name = "Analysis phase 2"
        project.owner = "Tester"
        project.status = "On Hold"
        
        db.session.commit(project)

        project = Projects.query.filter_by(id=2).first()

        self.assertNotEqual(project.project_name, "Coding")
        self.assertNotEqual(project.owner, "Admin")
        self.assertEqual(project.status, "Done")


    def test_update_task(self):
        task = Tasks.query.filter_by(id=2).first()

        task.task_name = "Phase 2"
        task.user = "Tester"
        task.status = "Under Process"

        db.session.commit(task)

        task = Tasks.query.filter_by(id=2).first()

        self.assertNotEqual(task.task_name, "Coding")
        self.assertNotEqual(task.user, "Admin")
        self.assertEqual(task.status, "Done")

class TestDelete(TestBase):

    def test_delete_project(self):
        project = Projects.query.filter_by(id=2).first()

        db.session.delete(project)              
        db.session.commit()

    def test_delete_task(self):
        task = Tasks.query.filter_by(id=2).first()

        db.session.delete(task)              
        db.session.commit()
       
class TestRoutes(TestBase):

    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page(self):
        response = self.client.get(url_for('projects'))
        self.assertEqual(response.status_code, 200)

    def test_tasks_page(self):
        response = self.client.get(url_for('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_addproject(self):
        target_url = url_for('addproject')
        redirect = url_for('projects', next=target_url)
        response = self.client.get(redirect)

        self.assertEqual(response.status_code, 200)
    
    def test_editproject(self):
        target_url = url_for('editproject')
        redirect = url_for('projects', next=target_url)
        response = self.client.get(redirect)

        self.assertEqual(response.status_code, 200)
    
    def test_addtask(self):
        target_url = url_for('addtask')
        redirect = url_for('projects', next=target_url)
        response = self.client.get(redirect)

        self.assertEqual(response.status_code, 302)
    
    def test_edittask(self):
        target_url = url_for('edittask')
        redirect = url_for('tasks', next=target_url)
        response = self.client.get(redirect)

        self.assertEqual(response.status_code, 302)