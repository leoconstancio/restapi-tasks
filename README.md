# About
Rest api with Django, DRF and Vue.JS.

## Requirements

```
Python 3, Django 2, PIP and VirtualEnv
```

### How to

Example install in Ubuntu:

```
#	virtualenv --python=python3 restapi-tasks
#	cd restapi-tasks && source bin/activate
#	git clone https://github.com/leoconstancio/restapi-tasks.git
#	pip install -r requirements.txt
#	python manage.py makemigrations
#	python manage.py migrate
#	python manage.py createsuperuser
#	python manage.py runserver

Run tests:
#   python manage.py test
```

Browser access: http://127.0.0.1:8000

##### API
```
GET ALL: /api/v1/tasks
GET ID: /api/v1/tasks/<id_task>
UPDATE: /api/v1/tasks/<id_task>
DELETE: /api/v1/tasks/<id_task>
POST: /api/v1/tasks
```