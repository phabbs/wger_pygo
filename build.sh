#!/bin/bash
python manage.py makemigrations
python manage.py migrate
gunicorn wger.wsgi --pythonpath=wger --log-file=-
