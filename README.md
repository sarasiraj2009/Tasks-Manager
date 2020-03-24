# Tasks-Manager
Introduction:

Projects Manager is a Web Application that improves the life of project managers, by tracking projects,tasks, users, status and deadlines in one place.
The result is the improved ability to manage complex tasks, especially for projects with multiple needs and requirements, as well as dealing with multiple projects that each have their own demands.

To create a CRUD application with utilisation of supporting tools and technologies to demonstrate modules covered in the first 5 weeks of the  training. The application has two tables with full CRUD functionality that allows the user to create, update, delete new project/task and display all projects and tasks.

Project planning and stories


Architecture
Entity Relationship Diagrams
Initial ERD plan

The initial plan contained more tables to make the Projects Manager Web Application  more effective by having Users can login to manage their Projects and tasks. And having a joint table will ease the tracking process of tasks.


Delivered ERD plan
Due to time constraints and working from distance, the Projects Manager Web Application ended up with building the 2 main tables Projects and Tasks, and creating a one to many relationship. Any Project has one or many tasks to be managed.



Testing
Testing has been done using pytest. The coverage report for the backend is 41%. Using pytest enabled me to test the application functionality, it needed a check to test the flow between the pages.

Deployment
Using Jenkins at the testing and deploymenting process for the Projects Manager Web Application made the process automated and with webhook to GitHub it made push and pull from the represoity is easy and triggered with every update on the code.
 

 
Used Technologies 
Database: GCP SQL Server
Programming language: Python
Framework: Flask
Deployment: Gunicorn
CI Server: Jenkins
Test Reporting: Pytest
VCS: GitHub
Project Tracking: Trello
Live Environment: GCP
 
Improvements for the Future
In Tasks report display Project Name instead of project id.
Display Tasks per Project.
Review the codes and minimize the duplicated codes(example: add project & edit project, ...etc.)
Have different users, to manage projects and tasks from any place.
Send reminder emails to users with deadlines.
Have Projects and Tasks timeline (history log).
Show Projects and Tasks in Calendar.
Have a board to easy access Projects and Tasks.
 
Author
Sara Mohamed
