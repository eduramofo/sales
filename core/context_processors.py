from django.utils import timezone
from datetime import timedelta
from event.models import Event
from account.models import Account
from django.db.models import Q


def globallabel(request):
    current_user = request.user
    result = None
    if current_user and not current_user.is_anonymous:
        result = 'bg-success'
        from_now_plus_1s = timezone.now() + timedelta(seconds=1)
        account = Account.objects.get(user=request.user)
        events_qs = Event.objects.filter(account=account, done=False, start_datetime__lte=from_now_plus_1s)
        if len(events_qs) > 0:
            result = 'bg-danger'
    return {'globallabel': result,}
