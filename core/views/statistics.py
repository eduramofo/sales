import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from leads.models import Lead


@login_required()
def statistics(request):

    page_title = 'Estatísticas'

    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'table_balance': table_balance,
    }

    return render(request, 'core/statistics/index.html', context)


def table_balance():

    table = {
        'totais': None,
        'em_aberto': None,
        'processados': None,
        'perdidos': None,
        'ganhos': None,
    }

    # totais
    totais = Lead.objects.all().count()
    table['totais'] = totais

    # quantidade_totais_de_leads_em_aberto
    query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')
    em_aberto = Lead.objects.filter(query).count()
    table['em_aberto'] = em_aberto

    # processados
    processados = totais - em_aberto
    table['processados'] = processados

    # perdidos
    perdidos = Lead.objects.filter(status='perdido').count()
    table['perdidos'] = perdidos

    # ganhos
    ganhos = Lead.objects.filter(status='ganho').count()
    table['ganhos'] = ganhos

    return table