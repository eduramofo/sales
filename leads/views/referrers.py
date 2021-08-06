from account.models import Account
from django.db.models import F, Q
from django.utils import timezone

from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from account.models import Account

from leads.process_contacts import gerar_leads
from leads.forms import ReferrerForm
from leads import models as leads_models
from leads.indicators import indicators_data

from core.tools import paginator


@login_required()
def referrers(request):
    leads = leads_models.Lead.objects.all()
    account = Account.objects.get(user=request.user)
    referrers = leads_models.Referrer.objects.filter(
        leads__in=leads, account=account).order_by(
            F('referring_datetime').desc(nulls_last=True),
    ).distinct()
    pages = paginator.make_paginator(request, referrers, 9)
    referrers = pages['page']
    nav_name = 'leads_referrers'
    page_title = 'Referenciadores'
    context = {
        'nav_name': nav_name,
        'page_title': page_title,
        'referrers': referrers,
        'page_range': pages['page_range'],
    }
    return render(request, 'leads/referrers/list_2/index.html', context)


@login_required()
def referrers_1(request):
    query = Q(status='novo') | Q(status='tentando_contato')
    leads = leads_models.Lead.objects.filter(query)
    account = Account.objects.get(user=request.user)
    referrers = leads_models.Referrer.objects.filter(
        leads__in=leads, account=account).order_by(
            F('referring_datetime').desc(nulls_last=True),
    ).distinct()
    pages = paginator.make_paginator(request, referrers, 9)
    referrers = pages['page']
    nav_name = 'leads_referrers'
    page_title = 'Referenciadores'
    context = {
        'nav_name': nav_name,
        'page_title': page_title,
        'referrers': referrers,
        'page_range': pages['page_range'],
    }
    return render(request, 'leads/referrers/list_2/index.html', context)


@login_required()
def referrers_2(request):
    query = Q(status='novo') | Q(status='tentando_contato') | Q(status='tentando_contato_2')
    leads = leads_models.Lead.objects.filter(query)
    account = Account.objects.get(user=request.user)
    referrers = leads_models.Referrer.objects.filter(
        leads__in=leads, account=account).order_by(
            F('referring_datetime').desc(nulls_last=True),
    ).distinct()
    pages = paginator.make_paginator(request, referrers, 9)
    referrers = pages['page']
    nav_name = 'leads_referrers'
    page_title = 'Referenciadores'
    context = {
        'nav_name': nav_name,
        'page_title': page_title,
        'referrers': referrers,
        'page_range': pages['page_range'],
    }
    return render(request, 'leads/referrers/list_2/index.html', context)


@login_required()
def leads_upload(request):
    indicated_by_datetime = timezone.localtime(timezone.now()).strftime('%Y-%m-%dT%H:%M')
    gmt = -3
    form = ReferrerForm()
    lead_id_raw = request.GET.get('lead', '')
    lead_name = ''
    lead_id = ''
    if lead_id_raw: 
        lead = get_object_or_404(leads_models.Lead, id=lead_id_raw)
        lead_name = str(lead)
        lead_id = str(lead.id)
    initial = {
        'name': lead_name,
        'referring_datetime': indicated_by_datetime,
        'gmt': gmt,
        'lead': lead_id,
    }
    form = ReferrerForm(initial=initial)
    if request.method == 'POST':
        form = ReferrerForm(request.POST)
        if form.is_valid():
            referrer = gerar_leads(form, request)
            message_text = 'Leads criados com sucesso =)'
            messages.add_message(request,messages.SUCCESS, message_text)
            return HttpResponseRedirect(reverse('leads:leads_referrers_edit', args=[str(referrer.id),]))
        else:
            message_text = 'Ocorreu um ERRO durante a inclusão dos Leads, faça uma verificação manual!'
            messages.add_message(request,messages.ERROR, message_text)
    context = {
        'nav_name': 'leads_upload',
        'form': form,
    }
    return render(request, 'leads/upload/index.html', context)


@login_required()
def referrers_old(request):
    indicators = indicators_data()
    nav_name = 'leads_referrers'
    page_title = 'Referenciadores'
    context = {
        'nav_name': nav_name,
        'page_title': page_title,
        'indicators': indicators,
    }
    return render(request, 'leads/indicators_list/index.html', context)
