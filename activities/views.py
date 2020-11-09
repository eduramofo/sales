from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from core.tools import paginator

from activities.models import Activity
from activities.forms import ActivityForm
from activities.filters import ActivityFilter


@login_required()
def activity_add(request):

    initial = {}
    activity_form = ActivityForm(initial=initial)
    page_title = 'Criação de uma nova atividade'
    nav_name = 'activities_list'

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

    return render(request, 'activities/add/index.html', context)


@login_required()
def activity_update(request, activity_id):

    activity = get_object_or_404(Activity, id=activity_id)
    activity_form = ActivityForm(request.POST or None, instance=activity, prefix='activity')
    page_title = 'Atualização de Atividade'
    nav_name = 'activities_list'
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
    
    nav_name = 'activities_list'
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
