from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def event_list_all(request):
    page_title = 'Eventos'
    events = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nav_name = 'event'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'events': events,
    }
    return render(request, 'event/event_list_all/index.html', context)


@login_required()
def event_list_open(request):
    page_title = 'Eventos em aberto'
    nav_name = 'event'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }
    return render(request, 'event/event_list_open/index.html', context)


@login_required()
def event_list_done(request):
    page_title = 'Eventos concluídos'
    nav_name = 'event'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }
    return render(request, 'event/event_list_done/index.html', context)


@login_required()
def event_list_overdue(request):
    page_title = 'Eventos vencidos'
    nav_name = 'event'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }
    return render(request, 'event/event_list_overdue/index.html', context)
