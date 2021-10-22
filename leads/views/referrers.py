from account.models import Account
from django.db.models import F, Q
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from account.models import Account
from leads import models as leads_models
from leads.models import LineGroup
from core.tools import paginator


@login_required()
def select_current_line_group(request):
    account = Account.objects.get(user=request.user)
    nav_name = 'leads_referrers'
    page_title = 'Seleção do Grupo de Linha'
    line_group = LineGroup.objects.filter(active=True, account=account).order_by('-default')
    line_group_id = request.GET.get('line-group-id', None)
    all_referrers_url = reverse('leads:referrers',)
    if line_group_id == 'all':
        account.current_line_group = None
        account.save()
        return HttpResponseRedirect(all_referrers_url)
    elif line_group_id:
        account.current_line_group = line_group.filter(id=line_group_id).first()
        account.save()
        return HttpResponseRedirect(all_referrers_url)
    context = {
        'nav_name': nav_name,
        'page_title': page_title,
        'line_group': line_group,
    }
    return render(request, 'leads/referrers/select_current_line_group/index.html', context)


@login_required()
def referrers(request):
    leads = leads_models.Lead.objects.all()
    account = Account.objects.get(user=request.user)
    current_line_group = account.current_line_group
    referrers = get_referrers(leads, current_line_group, account)
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
    current_line_group = account.current_line_group
    referrers = get_referrers(leads, current_line_group, account)
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
    current_line_group = account.current_line_group
    referrers = get_referrers(leads, current_line_group, account)
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


def get_referrers(leads, current_line_group, account):
    if current_line_group:
        referrers = leads_models.Referrer.objects.filter(
            leads__in=leads, account=account, line_group=current_line_group).order_by(
                F('referring_datetime').desc(nulls_last=True),
        ).distinct()
    else:
        referrers = leads_models.Referrer.objects.filter(
            leads__in=leads, account=account).order_by(
                F('referring_datetime').desc(nulls_last=True),
        ).distinct()
    return referrers
