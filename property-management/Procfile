web: gunicorn propertyManagement.wsgi —-log-file -
release: python manage.py makemigrations role && python manage.py migrate role && python manage.py makemigrations && python manage.py migrate