# Pitchme-test-task

A small flask application using flask-sqlalchemy, flask-login, bootstrap.


### Create Python virtual environment 
```
python3 -m venv venv
```
### Activate it
Run from `${project_root}:
```
. venv/bin/activate
```
### To deactivate run:
```
deactivate
```
### Install dependencies
Run from `${project_root}:
```
pip install -r requirements.txt
```
### Create the database:
```
python manage.py create-db
```
### To drop a database:
```
python manage.py drop-db
```
### Create admin:
```
python manage.py create-admin
```
### To load test database data:
```
python manage.py load-test-data
```
### To start it:
```
flask run
```

#### How the test task, the project was whipped up. many points have been omitted, somewhere there is untidiness. Only notifications to users by filters are not made  The project was completed in 5 days

# Plan for revision

- elimination of bugs  
- extracting a lot of logic from view functions  
- splitting html files into laconic templates  
- removing a lot of logic from templates  
- full form validation  
- changing hardcoded paths to url_for functions  
- moving the project configuration to a separate place  
- adding notifications about new events by saved filters using websockets
















