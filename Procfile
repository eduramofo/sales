release: python manage.py migrate --no-input
web: gunicorn --bind 0.0.0.0:$PORT sales.wsgi:application