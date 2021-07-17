from django.utils import timezone
import math
from datetime import timedelta
from activities.models import Activity
from analytics.data import get_conversations_day


def past_due_activities(request):
    result = False
    # from_now_plus_1s = timezone.now() + timedelta(seconds=1)
    # activities = Activity.objects.filter(
    #     done=False,
    #     due_date__lte=from_now_plus_1s,
    # ).exclude(lead=None).filter(lead__status='agendamento').order_by('due_date')
    # if len(activities) > 0: result = True
    return {'past_due_activities': result,}


def goal_of_the_day(request):
    conversations_goal = 30
    conversations = get_conversations_day()
    percentage = conversations / conversations_goal
    percentage_int = int(math.floor(percentage*100))
    percentage_int_str = str(percentage_int)
    percentage_str = str(percentage_int) + '%'
    result = {
        'conversations_goal': conversations_goal,
        'conversations': conversations,
        'percentage': percentage,
        'percentage_int': percentage_int,
        'percentage_int_str': percentage_int_str,
        'percentage_str': percentage_str,
    }
    return {'goal_of_the_day': result,}
