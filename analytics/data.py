from datetime import datetime, timedelta
from django.utils.timezone import utc
from conversation.models import Conversation


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
