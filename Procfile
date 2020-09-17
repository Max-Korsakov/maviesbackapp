release: python manage.py makemigrations  --no-input
release: python manage.py migrate --no-input
release: python manage.py loaddata movies.json
web: gunicorn movie_backend.wsgi