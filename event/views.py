from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from core.tools import paginator
from account.models import Account
from event.models import Event
from event.forms import EventForm


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
    page_title = 'Eventos Em Aberto'
    nav_name = 'event'
    account = Account.objects.get(user=request.user)
    events_qs = Event.objects.filter(account=account, done=False)
    pages = paginator.make_paginator(request, events_qs, 20)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'events': pages['page'],
        'page_range': pages['page_range'],
    }
    return render(request, 'event/event_list_open/index.html', context)


@login_required()
def event_list_done(request):
    page_title = 'Eventos Concluídos'
    nav_name = 'event'
    account = Account.objects.get(user=request.user)
    events_qs = Event.objects.filter(account=account, done=True)
    pages = paginator.make_paginator(request, events_qs, 20)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'events': pages['page'],
        'page_range': pages['page_range'],
    }
    return render(request, 'event/event_list_done/index.html', context)


@login_required()
def event_list_overdue(request):
    page_title = 'Eventos Vencidos'
    nav_name = 'event'
    account = Account.objects.get(user=request.user)
    from_now_plus_1s = timezone.now() + timedelta(seconds=1)
    events_qs = Event.objects.filter(account=account, done=False, start_datetime__lte=from_now_plus_1s)
    pages = paginator.make_paginator(request, events_qs, 20)
    for n in range(150):
        Event.objects.create(
            summary='Evento Teste ' + str(n),
        )
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'events': pages['page'],
        'page_range': pages['page_range'],
    }
    return render(request, 'event/event_list_overdue/index.html', context)


@login_required()
def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    page_title = 'Evento: ' + event.summary
    nav_name = 'event'
    event_form = EventForm(request.POST or None, instance=event)
    method = request.method
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'event_form': event_form,
        'event': event,
    }
    if method == 'POST':
        if event_form.is_valid():
            event = event_form.save()
            url = reverse_lazy('event:event_update', args=(str(event.id),))
            messages.add_message(request, messages.SUCCESS, 'Atividade atualizado com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário da atividade!')
    return render(request, 'event/event_update/index.html', context)
