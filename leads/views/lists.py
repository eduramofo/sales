from datetime import timedelta

from django.utils import timezone
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy

from core.tools import paginator
from activities.models import Activity

from account.models import Account
from leads.models import Lead
from leads.filters import LeadFilter
from leads import tools


@login_required()
def home(request):
    nav_name = 'leads_list'
    page_title = 'Listas de Leads'
    priorities = {'title': 'Prioridades', 'url': 'leads:lists:priorities'}
    all = {'title': 'Todos', 'url': 'leads:lists:all'}
    news = {'title': 'Novos', 'url': 'leads:lists:news'}
    opened = {'title': 'Abertos', 'url': 'leads:lists:opened'}
    flow = {'title': 'Flow', 'url': 'leads:lists:flow'}
    bolo_1 = {'title': 'Bolos 1', 'url': 'leads:lists:ghosting'}
    bolo_2 = {'title': 'Bolos 2', 'url': 'leads:lists:ghosting_2'}
    off_1 = {'title': 'Offs 1', 'url': 'leads:lists:off'}
    off_2 = {'title': 'Offs 2', 'url': 'leads:lists:off_2'}
    lists = [
        all, priorities, news, opened, flow, bolo_1, bolo_2, off_1, off_2,
    ]

    context = {
        'page_title': page_title,
        'lists': lists,
    }

    return render(request, 'leads/list/home/index.html', context)


@login_required()
def search(request):

    nav_name = 'leads_list'

    page_title = 'Pesquisa de Leads'
    
    account = Account.objects.get(user=request.user)

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(account=account).order_by('-created_at'))

    form = leads.form

    pages = paginator.make_paginator(request, leads.qs, 5)
    
    page = pages['page']

    if len(page) == 1:
        lead_id_str = str(page[0].id)
        url = reverse_lazy('leads:update', args=(lead_id_str,))
        return HttpResponseRedirect(url)

    context = {
        'page_title': page_title,
        'leads': page,
        'page_range': pages['page_range'],
        'nav_name': nav_name,
        'leads_filters_form': form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def all(request):
    
    nav_name = 'leads_list'

    page_title = 'Leads'
    
    account = Account.objects.get(user=request.user)

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(account=account).order_by('-created_at'))

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

    account = Account.objects.get(user=request.user)

    leads_queryset = tools.get_open_run_now_leads(account)

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

    page_title = 'Leads Novos'

    account = Account.objects.get(user=request.user)

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(account=account, status='novo').order_by('-priority'))

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

    page_title = 'Leads em aberto'

    query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')
    
    account = Account.objects.get(user=request.user)

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(account=account).filter(query).order_by('-priority'))

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
    
    account = Account.objects.get(user=request.user)

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(account=account, priority=True).filter(query).order_by('-created_at'))

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

    page_title = 'Leads em agendamentos abertos'

    from_now_plus_24h = timezone.now() + timedelta(days=1)

    account = Account.objects.get(user=request.user)

    ########################################

    activities = Activity.objects.filter(
        account=account,
        done=False,
        due_date__lte=from_now_plus_24h,
    ).exclude(lead=None).order_by('due_date')

    leads_pks= []
    leads___ = []
    for activity in activities:
        lead = activity.lead
        if lead.status == 'agendamento' or lead.status == 'agendamento_direct':
            leads_pks.append(lead.pk)
            leads___.append(lead)

    ########################################

    query = Q(status='agendamento') | Q(status='agendamento_direct')

    leads_ = Lead.objects.filter(account=account, pk__in=leads_pks).filter(query).order_by('name')

    leads = LeadFilter(request.GET, queryset=leads_)

    pages = paginator.make_paginator(request, leads.qs, 50)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': leads___,
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def ghosting(request):
    
    nav_name = 'leads_list'

    page_title = 'Leads Bolo 1'
    
    account = Account.objects.get(user=request.user)
    
    queryset = Lead.objects.filter(account=account, status='ghosting').order_by('-created_at')

    leads = LeadFilter(request.GET, queryset=queryset)

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
def ghosting_2(request):
    
    nav_name = 'leads_list'

    page_title = 'Leads Bolo 2'
    
    account = Account.objects.get(user=request.user)

    queryset = Lead.objects.filter(account=account, status='ghosting_2').order_by('-created_at')

    leads = LeadFilter(request.GET, queryset=queryset)

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
def off(request):
    
    nav_name = 'leads_list'

    page_title = 'Leads Off 1'

    account = Account.objects.get(user=request.user)

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(account=account, status='off').order_by('-created_at'))

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
def off_2(request):

    nav_name = 'leads_list'

    page_title = 'Leads Off 2'
    
    account = Account.objects.get(user=request.user)

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(account=account, status='off_2').order_by('-created_at'))

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)
