release: python manage.py migrate --no-input
web: gunicorn --bind 0.0.0.0:$PORT sales.wsgi:application
worker: celery -A sales worker --pool=solo -l info -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
