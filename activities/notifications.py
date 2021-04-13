from django.utils import timezone
from datetime import timedelta
from activities.models import Activity


def schedule_notification():
    now = timezone.now()
    activities = Activity.objects.filter(
        done=False,
        due_date__lte=now,
    ).exclude(lead=None).exclude(notification_sent=False).filter(lead__status='agendamento').order_by('due_date')
    for current_activity in activities:
        msg = 'Agendamento: João da Silva 15 de Janeiro de 2021 às 21'
        msg = 'Vou atrasar'
        msg = 'Abrir lead'
        print(current_activity)
