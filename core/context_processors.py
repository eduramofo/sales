from django.utils import timezone
from datetime import timedelta
from activities.models import Activity


def past_due_activities(request):
    result = False
    from_now_plus_1s = timezone.now() + timedelta(seconds=1)
    activities = Activity.objects.filter(
        done=False,
        due_date__lte=from_now_plus_1s,
    ).exclude(lead=None).filter(lead__status='agendamento').order_by('due_date')
    if len(activities) > 0: result = True
    return {'past_due_activities': result,}
