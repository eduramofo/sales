from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)
