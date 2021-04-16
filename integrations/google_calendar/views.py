import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . import calendar


@login_required()
def oauth2(request):

    calendar.setup()

    data = {
        'success': True,
    }

    return JsonResponse(data)


@login_required()
def oauth2callback(request):

    data = {
        'success': True,
    }

    return JsonResponse(data)
