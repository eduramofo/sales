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
from django.forms import formset_factory


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

    leads = referrer_obj.leads.order_by('-priority', 'name')

    page_title = 'Editar Leads do(a) {}'.format(referrer_obj)

    LeadSimpleFormset = formset_factory(LeadSimpleForm, extra=0)

    if request.method == 'POST':
        lead_simple_formset = LeadSimpleFormset(request.POST)
        if lead_simple_formset.is_valid():
            for lead_data in lead_simple_formset.cleaned_data:
                lead_obj = get_object_or_404(Lead, id=lead_data['lead_id'])
                lead_obj.status = lead_data['status']
                lead_obj.name = lead_data['name']
                lead_obj.nickname = lead_data['nickname']
                lead_obj.gender = lead_data['gender']
                lead_obj.priority = lead_data['priority']
                lead_obj.tel = lead_data['tel']
                lead_obj.waid = lead_data['waid']
                lead_obj.note = lead_data['note']
                lead_obj.location = lead_data['location']
                lead_obj.gmt = lead_data['gmt']
                lead_obj.save()
        message_text = 'Leads atualizados com sucesso!'
        messages.add_message(request, messages.SUCCESS, message_text)
        return HttpResponseRedirect(reverse('leads:leads_referrers_edit', args=[str(referrer_obj.id),]))

    else:
        lead_simple_formset_initial = []
        for lead in leads:
            lead_simple_formset_initial.append(
                {
                    'lead_id': lead.id,
                    'status': lead.status,
                    'gender': lead.gender,
                    'priority': lead.priority,
                    'tel': lead.tel,
                    'waid': lead.waid,
                    'note': lead.note,
                    'name': lead.name,
                    'location': lead.location,
                    'gmt': lead.gmt,
                    'nickname': lead.nickname,
                }
            )
        lead_simple_formset = LeadSimpleFormset(initial=lead_simple_formset_initial)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'formset': lead_simple_formset,
        'referrer': referrer_obj,
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

    # T1
    leads = referrer_obj.leads.filter(status='novo').order_by('order', '-priority')
    if len(leads) > 0:
        lead = leads.first()
        redirect_url = reverse_lazy('leads:update', args=(str(lead.id),))
        return HttpResponseRedirect(redirect_url)

    # T2
    leads = referrer_obj.leads.filter(status='tentando_contato').order_by('order', '-priority')
    if len(leads) > 0:
        lead = leads.first()
        redirect_url = reverse_lazy('leads:update', args=(str(lead.id),))
        return HttpResponseRedirect(redirect_url)
    
    # T3
    leads = referrer_obj.leads.filter(status='tentando_contato_2').order_by('order', '-priority')
    if len(leads) > 0:
        lead = leads.first()
        redirect_url = reverse_lazy('leads:update', args=(str(lead.id),))
        return HttpResponseRedirect(redirect_url)

    # ALL
    redirect_url = reverse_lazy('leads:leads_referrers_all', args=(str(referrer_obj.id),))

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
