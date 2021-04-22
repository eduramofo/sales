import json

from django.utils.timezone import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from core import telegram
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

    activities_count = activities.count()

    leads_count = leads.count()

    leads_win = leads.filter(status='ganho').count()

    #### LOST
    leads_lost = leads.filter(status='perdido').count()
    leads_lost_sem_interesse = leads.filter(status='perdido', status_lost_justification='sem_interesse').count()
    leads_lost_sem_dinheiro = leads.filter(status='perdido', status_lost_justification='interessado_sem_condicoes_financeiras').count()
    leads_lost_di = leads.filter(status='perdido', status_lost_justification='di').count()
    leads_lost_entrevista = leads.filter(status='perdido', status_lost_justification='entrevista_perdida').count()


    # activities
    table['activities'] = activities_count

    # LEADS TOTAL
    table['leads_processed'] = leads_count

    table['leads_processed_per'] = 'N/A'
    if leads_count != 0:
        table['leads_processed_per'] = round(leads_count / leads_count * 100, 2)

    # LEADS LOST
    table['leads_lost'] = leads_lost
    table['leads_lost_per'] = 'N/A'
    if leads_count != 0:
        table['leads_lost_per'] = round(leads_lost / leads_count * 100, 2)

    # LEADS LOST - SEM INTERESSE
    table['leads_lost_sem_interesse'] = leads_lost_sem_interesse
    table['leads_lost_sem_interesse_per'] = 'N/A'
    if leads_count != 0:
        table['leads_lost_sem_interesse_per'] = round(leads_lost_sem_interesse / leads_count * 100, 2)

    # LEADS LOST - DI
    table['leads_lost_di'] = leads_lost_sem_interesse
    table['leads_lost_di_per'] = 'N/A'
    if leads_count != 0:
        table['leads_lost_di_per'] = round(leads_lost_sem_interesse / leads_count * 100, 2)

    # LEADS LOST - ENTREVISTAS
    table['leads_lost_entrevistas'] = leads_lost_entrevista
    table['leads_lost_entrevistas_per'] = 'N/A'
    if leads_count != 0:
        table['leads_lost_entrevistas_per'] = round(leads_lost_entrevista / leads_count * 100, 2)

    # OTHERS
    table['leads_win'] = leads_win

    table['leads_win_per'] = 'N/A'
    table['activities_leads'] = 'N/A'
    if leads_count != 0:
        table['leads_win_per'] = round(leads_win / leads_count * 100, 2)
        table['activities_leads'] = round(activities_count / leads_count, 2)

    # LEADS LOST LOST
    leads_lost_lost_sem_interesse_per = 'N/A'
    leads_lost_lost_sem_dinheiro_per = 'N/A'
    leads_lost_lost_di_per = 'N/A'
    if leads_lost != 0:
        leads_lost_lost_sem_interesse_per = round(leads_lost_sem_interesse / leads_lost * 100, 2)
        leads_lost_lost_sem_dinheiro_per = round(leads_lost_sem_dinheiro / leads_lost * 100, 2)
        leads_lost_lost_di_per = round(leads_lost_di / leads_lost * 100, 2)
        leads_lost_lost_entrevista_per = round(leads_lost_entrevista / leads_lost * 100, 2)
        table['leads_lost_lost_per'] = round(leads_lost / leads_lost * 100, 2)
        table['leads_lost_lost_sem_interesse'] = leads_lost_sem_interesse
        table['leads_lost_lost_sem_interesse_per'] = leads_lost_lost_sem_interesse_per
        table['leads_lost_lost_sem_dinheiro'] = leads_lost_sem_dinheiro
        table['leads_lost_lost_sem_dinheiro_per'] = leads_lost_lost_sem_dinheiro_per
        table['leads_lost_lost_di'] = leads_lost_di
        table['leads_lost_lost_di_per'] = leads_lost_lost_di_per
        table['leads_lost_lost_entrevista'] = leads_lost_entrevista
        table['leads_lost_lost_entrevista_per'] = leads_lost_lost_entrevista_per

    table['kpi_entrevistas'] = leads_lost_entrevista + leads_win


    table['kpi_perdidos_entrevistas'] = 'N/A'
    if (leads_lost_entrevista + leads_win) != 0:
        table['kpi_perdidos_entrevistas'] = round(leads_count / (leads_lost_entrevista + leads_win), 1)

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
