from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone

from core.tools import paginator

from activities.models import Activity
from activities.forms import ActivityForm
from activities.filters import ActivityFilter

from leads import models as LeadsModels


@login_required()
def add_through_lead(request, lead_id):

    shortcut = request.GET.get('shortcut', None)

    lead = get_object_or_404(LeadsModels.Lead, id=lead_id)

    prefix_activity_form = 'activity_add_through_lead'

    due_date = timezone.now().strftime('%Y-%m-%dT%H:%M')

    subject = None

    type_ = 'call'

    if shortcut == 'nao-atendeu':
        subject = 'Não atendeu'
    if shortcut == 'sem-interesse':
        subject = 'Sem interesse'
    if shortcut == 'sem-dinheiro':
        subject = 'Sem condições financeiras'

    initial_activity_initial = {
        'lead': str(lead.id),
        'due_date': due_date,
        'done': True,
        'subject': subject,
        'type': type_,
    }

    activity_form = ActivityForm(
        initial=initial_activity_initial,
        prefix=prefix_activity_form,
    )

    page_title = 'Criação de atividade para o Lead {}'.format(lead)

    nav_name = 'activities'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'activity_form': activity_form,
        'lead': lead,
    }

    if request.method == 'POST':
        activity_form = ActivityForm(request.POST, prefix=prefix_activity_form)
        if activity_form.is_valid():
            activity = activity_form.save()
            url = reverse_lazy('leads:update', args=(str(lead.id),))
            messages.add_message(request, messages.SUCCESS, 'Atividade criada com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Há erro(s) no formulário de atividade.')
            context['activity_form'] = activity_form

    return render(request, 'activities/leads/add_through_lead/index.html', context)


@login_required()
def activity_add(request, lead_id):

    initial = {
        'lead': lead_id,
    }

    activity_form = ActivityForm(initial=initial, prefix="activity-lead")
    page_title = 'Criação de uma nova atividade'
    nav_name = 'activities'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'activity_form': activity_form,
    }

    if request.method == 'POST':
        activity_form = ActivityForm(request.POST)
        if activity_form.is_valid():
            activity = activity_form.save()
            url = reverse_lazy('activities:update', args=(str(activity.id),))
            messages.add_message(request, messages.SUCCESS, 'Atividade criada com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário da atividade!')
            context['activity_form'] = activity_form

    return render(request, 'activities/leads/add.html', context)


@login_required()
def activity_update(request, activity_id):

    activity = get_object_or_404(Activity, id=activity_id)
    activity_form = ActivityForm(request.POST or None, instance=activity, prefix='activity')
    page_title = 'Atualização de Atividade'
    nav_name = 'activities'
    method = request.method

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'activity': activity,
        'activity_form': activity_form,
    }

    if method == 'POST':
        if activity_form.is_valid():
            activity = activity_form.save()
            url = reverse_lazy('activities:update', args=(str(activity.id),))
            messages.add_message(request, messages.SUCCESS, 'Atividade atualizado com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário da atividade!')

    return render(request, 'activities/update/index.html', context)


@login_required()
def activities_list(request):
    
    nav_name = 'activities'
    page_title = 'Lista de Atividades'
    activities = ActivityFilter(request.GET, queryset=Activity.objects.all().order_by('-created_at'))
    pages = paginator.make_paginator(request, activities.qs, 10)

    context = {
        'page_title': page_title,
        'activities': pages['page'],
        'page_range': pages['page_range'],
        'nav_name': nav_name,
        'activities_filters_form': activities.form,
    }

    return render(request, 'activities/list/index.html', context)
