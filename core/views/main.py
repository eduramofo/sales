import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


@login_required()
def index(request):

    context = {
        'page_title': 'Home',
        'nav_name': 'core_home'
    }

    return render(request, 'core/home/index.html', context)


def messages(request):
    context = {}
    messages_html = render_to_string('core/tools/messages.html', context, request)
    if len(messages_html) == 1:
        messages_html = None
    data = {
        'messages': messages_html,
    }
    return JsonResponse(data)


def speech(request):
    return render(request, 'speech/index.html', {})

