from django.contrib.auth.models import User
from activities.models import Activity
from conversation.models import Conversation
from event.models import Event


# python manage.py shell
# from core import deploy
# deploy.go()
def go():
    edu = User.objects.get(username='edu')
    Activity.objects.all().update(account=edu)
    Conversation.objects.all().update(account=edu)
    Event.objects.all().update(account=edu)
    print('Gooooo!')
