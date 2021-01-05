import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


def settings(request):

    page_title = 'Configurações'
    nav_name = 'settings'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'core/settings/index.html', context)
