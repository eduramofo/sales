import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from integrations import google_calendar


@login_required()
def oauth2(request):

    google_calendar.calendar.setup()

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
