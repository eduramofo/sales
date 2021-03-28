import json

from django.utils.timezone import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from leads import models as leads_models
from activities.models import Activity


@login_required()
def home(request):

    page_title = 'Estatísticas (Home)'

    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'statistics/home/index.html', context)


@login_required()
def balance(request):

    page_title = 'Estatísticas (Balanço dos Leads)'

    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'table_balance': table_balance(),
    }

    return render(request, 'statistics/balance/index.html', context)


@login_required()
def day_detail(request):

    page_title = 'Estatísticas (Detalhe de um Dia)'

    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    day_detail_date_str = request.GET.get('day-detail-date', None)
    if day_detail_date_str:
        day_detail_date_url = reverse_lazy('core:statistics_day_detail_result', args=(day_detail_date_str,))
        return HttpResponseRedirect(day_detail_date_url)

    return render(request, 'statistics/day_detail/index.html', context)


@login_required()
def day_detail_result(request, dt):

    dt_obj = datetime.strptime(dt, '%Y-%m-%d')
    
    activities = Activity.objects.filter(
        created_at__year=dt_obj.year,
        created_at__month=dt_obj.month,
        created_at__day=dt_obj.day
    )
    
    page_title = 'Estatísticas (Detalhe de um Dia | Resultado)'

    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'activities': activities,
        'abstract': abstract(dt_obj),
    }

    return render(request, 'statistics/day_detail_result/index.html', context)


def abstract(dt_obj):

    table = {
        'leads_processed': None,
        'leads_lost': None,
        'activities': None,
    }

    activities = Activity.objects.filter(
        created_at__year=dt_obj.year,
        created_at__month=dt_obj.month,
        created_at__day=dt_obj.day
    )

    leads_pks = leads_processed = activities.values_list('lead', flat=True).distinct()

    leads = leads_models.Lead.objects.filter(pk__in=leads_pks)

    table['leads_processed'] = leads.count()

    table['leads_lost'] = leads.filter(status='perdido').count()

    table['activities'] = activities.count()

    return table


def table_balance():

    table = {
        'totais': None,
        'em_aberto': None,
        'processados': None,
        'perdidos': None,
        'ganhos': None,
    }

    # totais
    totais = leads_models.Lead.objects.all().count()
    table['totais'] = totais

    # quantidade_totais_de_leads_em_aberto
    query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')
    em_aberto = leads_models.Lead.objects.filter(query).count()
    table['em_aberto'] = em_aberto

    # processados
    processados = totais - em_aberto
    table['processados'] = processados

    # perdidos
    perdidos = leads_models.Lead.objects.filter(status='perdido').count()
    table['perdidos'] = perdidos

    # ganhos
    ganhos = leads_models.Lead.objects.filter(status='ganho').count()
    table['ganhos'] = ganhos

    return table
