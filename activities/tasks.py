from celery import Celery
from django_celery_results.models import TaskResult

from activities import notifications

app = Celery()

@app.task
def sync_orcamentos():
    notifications.schedule_notification()


@app.task
def clear_celery_backend_result():
    TaskResult.objects.all().delete()
