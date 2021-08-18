from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.tools import paginator
from event.models import Event
from account.models import Account


@login_required()
def event_list_all(request):
    page_title = 'Eventos'
    nav_name = 'event'
    account = Account.objects.get(user=request.user)
    events_qs = Event.objects.filter(account=account)
    pages = paginator.make_paginator(request, events_qs, 20)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'events': pages['page'],
        'page_range': pages['page_range'],
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
    for n in range(150):
        Event.objects.create(
            summary='Evento Teste ' + str(n),
        )
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }
    return render(request, 'event/event_list_overdue/index.html', context)


@login_required()
def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    page_title = 'Evento: ' + event.summary
    nav_name = 'event'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'event': event,
    }
    return render(request, 'event/event_update/index.html', context)
