from django.utils import timezone
from urllib.parse import urlencode
from random import choice as random_choice

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
from leads.forms import LeadForm, LeadFormRunNow, ReferrerForm, LeadSimpleForm
from leads.filters import LeadFilter
from leads import tools
from leads.templatetags import leads_extras


@login_required()
def referrers_edit(request, referrer_id):

    nav_name = 'leads_list'

    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads = referrer_obj.leads.order_by('name')

    page_title = 'Editar Leads do(a) {}'.format(referrer_obj)

    lead_simple_form = LeadSimpleForm()

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': leads,
        'lead_simple_form': lead_simple_form,
    }

    return render(request, 'leads/referrers/list_edit/index.html', context)


@login_required()
def referrers_all(request, referrer_id):

    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads = referrer_obj.leads

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_closed(request, referrer_id):

    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='perdido') | Q(status='ganho')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads fechados leads do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_opened(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando') | Q(status='agendamento') | Q(status='acompanhamento')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads abertos do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_news(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='novo')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads novos do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_agendamento(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='agendamento')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)
    
    page_title = 'Leads  do: {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_follow_up(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='acompanhamento')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)
    
    page_title ='Leads em acompanhamento perdidos do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_ganho(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='ganho')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)
    
    page_title = 'Leads ganho(s) do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_perdido(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='perdido')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)
    
    page_title = 'Leads perdido(s) do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_next(request, referrer_id):

    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    # ALL
    redirect_url = reverse_lazy('leads:leads_referrers_all', args=(str(referrer_obj.id),))

    # T3
    leads = referrer_obj.leads.filter(status='tentando_contato_2').order_by('-priority')
    if len(leads) > 0:
        lead = leads.first()
        redirect_url = reverse_lazy('leads:update', args=(str(lead.id),))

    # T2
    leads = referrer_obj.leads.filter(status='tentando_contato').order_by('-priority')
    if len(leads) > 0:
        lead = leads.first()
        redirect_url = reverse_lazy('leads:update', args=(str(lead.id),))

    # T1
    leads = referrer_obj.leads.filter(status='novo').order_by('-priority')
    if len(leads) > 0:
        lead = leads.first()
        redirect_url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(redirect_url)


@login_required()
def referrers_tentando(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='tentando_contato')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads tentando do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_t1(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='novo')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads T1 do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_t2(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='tentando_contato')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads T2 do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_t3(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='tentando_contato_2')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads T3 do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def referrers_cnr(request, referrer_id):
    
    nav_name = 'leads_list'
    
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads_filter_query = Q(status='geladeira')

    leads = referrer_obj.leads.filter(leads_filter_query)

    leads = LeadFilter(
        request.GET, queryset=leads.order_by('-priority')
    )

    pages = paginator.make_paginator(request, leads.qs, 50)

    page_title = 'Leads T3 do(a) {}'.format(referrer_obj)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)
