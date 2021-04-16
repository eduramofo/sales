import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse

from . import authorize
from . import events


@login_required()
def oauth2(request):
    authorization_url = authorize.authorize(request)
    return HttpResponseRedirect(authorization_url)


@login_required()
def oauth2callback(request):
    success_url = authorize.callback(request)
    return HttpResponseRedirect(success_url)


@login_required()
def oauth2success(request):
    data = authorize.success()
    return JsonResponse(data)
