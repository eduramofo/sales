import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


@login_required()
def home(request):

    context = {
        'page_title': 'Academia',
        'nav_name': 'core_home'
    }

    return render(request, 'academy/index.html', context)
