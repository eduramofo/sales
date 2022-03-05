from celery import shared_task
from analytics.daily_report import daily_report_run


@shared_task
def daily_report():
    daily_report_run()
