import json

from django.utils.timezone import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from leads import models as leads_models
from activities.models import Activity


@login_required()
def statistics(request):

    page_title = 'Estatísticas'

    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'table_balance': table_balance(),
        'table_productivity': table_productivity(),
    }

    return render(request, 'core/statistics/index.html', context)


def table_productivity():

    table = {
        'leads_processed': None,
        'leads_lost': None,
    }

    today = datetime.today()

    activities = Activity.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month,
        created_at__day=today.day
    )

    leads_pks = leads_processed = activities.values_list('lead', flat=True).distinct()
    leads = leads_models.Lead.objects.filter(pk__in=leads_pks)
    table['leads_processed'] = leads.count()
    table['leads_lost'] = leads.filter(status='perdido').count()

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
