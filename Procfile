web: gunicorn propertyManagement.wsgi —-log-file -
release: pipenv --python 3 install -r requirements.txt && python manage.py makemigrations --noinput && python manage.py migrate --noinput