from django.contrib.auth.models import User
from account.models import Account
from leads.models import Lead, Referrer


# python manage.py shell
# from core import deploy
# deploy.r1()
# deploy.r2()
# deploy.r3()
def r1():
    edu = User.objects.get(username='edu')
    Account.objects.create(user=edu)
    print("Sucesso em R1")

def r2():
    edu = User.objects.get(username='edu')
    Referrer.objects.all().update(account=edu)
    print("Sucesso em R2")

def r3():
    edu = User.objects.get(username='edu')
    Lead.objects.all().update(account=edu)
    print("Sucesso em R3")
