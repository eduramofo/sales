from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):

    context = {
        'page_title': 'Home',
        'nav_name': 'core_home'
    }

    return render(request, 'core/home/index.html', context)


@login_required()
def statistics(request):

    page_title = 'Estatísticas'
    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'core/statistics/index.html', context)


def settings(request):

    page_title = 'Configurações'
    nav_name = 'settings'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'core/settings/index.html', context)
