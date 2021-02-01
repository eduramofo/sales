from django.utils import timezone
from urllib.parse import urlencode
from random import choice as random_choice
from datetime import timedelta

from django.utils import timezone
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages


from core.tools import paginator

from activities.models import Activity

from leads.process_contacts import gerar_leads
from leads.models import Lead, Referrer
from leads.forms import LeadForm, LeadFormRunNow, ReferrerForm
from leads.filters import LeadFilter
from leads import tools
from leads.templatetags import leads_extras


@login_required()
def all(request):
    
    nav_name = 'leads_list'

    page_title = 'Lista de Leads'
    
    leads = LeadFilter(request.GET, queryset=Lead.objects.all().order_by('-created_at'))

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'nav_name': nav_name,
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def now(request):
    
    nav_name = 'leads_now'

    page_title = 'Lista de Leads [ AGORA ]'

    leads_queryset = tools.get_open_run_now_leads()

    leads = LeadFilter(request.GET, queryset=leads_queryset)

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def news(request):
    
    nav_name = 'leads_news'

    page_title = 'Lista de Novos Leads'

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(status='novo').order_by('-priority'))

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def opened(request):
    
    nav_name = 'leads_opened'

    page_title = 'Lista de Leads em Aberto'

    query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(query).order_by('-priority'))

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def priorities(request):
    
    nav_name = 'leads_priorities'

    page_title = 'Leads prioritários em aberto'

    query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(priority=True).filter(query).order_by('-created_at'))

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def schedules(request):

    nav_name = 'leads_schedules'

    page_title = 'Lista de Leads em Agendamentos'

    from_now_plus_24h = timezone.now() + timedelta(days=1)

    activities = Activity.objects.filter(
        done=False,
        due_date__lte=from_now_plus_24h,
    ).exclude(lead=None).order_by('due_date')
   
    leads_pks= []
    leads___ = []
    for activity in activities:
        lead = activity.lead
        if lead.status == 'agendamento':
            leads_pks.append(lead.pk)
            leads___.append(lead)

    leads_ = Lead.objects.filter(pk__in=leads_pks, status='agendamento')

    leads = LeadFilter(request.GET, queryset=leads_)

    pages = paginator.make_paginator(request, leads.qs, 1000)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': leads___,
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)