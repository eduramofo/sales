from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):

    context = {
        'page_title': 'Home',
        'nav_name': 'core_home'
    }

    return render(request, 'core/home/index.html', context)
