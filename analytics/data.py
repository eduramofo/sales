from datetime import datetime, timedelta
from django.utils.timezone import utc
from conversation.models import Conversation
from django.utils.timezone import datetime, make_aware, timedelta
from activities.models import Activity


def get_conversations_day():
    now = datetime.now()
    today = now.date()
    year = today.year
    month = today.month
    day = today.day
    conversation_day_qs = Conversation.objects.filter(
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    leads = conversation_day_qs.values_list('lead', flat=True).distinct().count()
    return leads


def get_activities_by_day(dt):
    dt_obj = make_aware(datetime.strptime(dt, '%Y-%m-%d'))
    activities = Activity.objects.filter(
        created_at__year=dt_obj.year,
        created_at__month=dt_obj.month,
        created_at__day=dt_obj.day
    ).exclude(subject='Inválido')
    return activities


def get_conversations_by_day(dt):
    dt_obj = make_aware(datetime.strptime(dt, '%Y-%m-%d'))
    year = dt_obj.year
    month = dt_obj.month
    day = dt_obj.day
    conversation_day_qs = Conversation.objects.filter(
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    leads = conversation_day_qs.values_list('lead', flat=True).distinct().count()
    return leads


def speechs_by_day(dt):
    dt_obj = make_aware(datetime.strptime(dt, '%Y-%m-%d'))
    year = dt_obj.year
    month = dt_obj.month
    day = dt_obj.day
    conversation_day_qs = Conversation.objects.filter(
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
        type__in=['lost', 'win', 'off'],
    )
    leads = conversation_day_qs.values_list('lead', flat=True).distinct().count()
    return leads


def win_by_day(dt):
    dt_obj = make_aware(datetime.strptime(dt, '%Y-%m-%d'))
    year = dt_obj.year
    month = dt_obj.month
    day = dt_obj.day
    conversation_day_qs = Conversation.objects.filter(
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
        type='win',
    )
    leads = conversation_day_qs.values_list('lead', flat=True).distinct().count()
    return leads
