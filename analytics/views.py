from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.timezone import datetime

from activities.models import Activity
from analytics import day


@login_required()
def home(request):

    page_title = 'Análise de Dados'

    nav_name = 'statistics'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'analytics/home/index.html', context)


@login_required()
def today(request):
    dts = datetime.now().strftime('%Y-%m-%d')
    url = reverse_lazy('analytics:day_result', args=(dts,))
    return HttpResponseRedirect(url)


@login_required()
def this_week(request):
    dts = datetime.now().strftime('%Y-%m-%d')
    dte = datetime.now().strftime('%Y-%m-%d')
    url = reverse_lazy('analytics:range_result', args=(dts,dte,))
    return HttpResponseRedirect(url)


@login_required()
def day_select(request):

    page_title = 'Análise de Dados'

    nav_name = 'analyze'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'analytics/home/index.html', context)


@login_required()
def day_result(request, dt):
    
    dt_obj = datetime.strptime(dt, '%Y-%m-%d')
    
    activities = Activity.objects.filter(
        created_at__year=dt_obj.year,
        created_at__month=dt_obj.month,
        created_at__day=dt_obj.day
    )

    page_title = 'Análise de Dados do Dia ' + dt_obj.strftime('%d de %B de %Y')

    nav_name = 'analyze'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'data': day.get_data_clean(activities),
    }

    return render(request, 'analytics/day_result/index.html', context)


@login_required()
def range_select(request):

    page_title = 'Análise de Dados'

    nav_name = 'analyze'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'analytics/home/index.html', context)


@login_required()
def range_result(request, dts, dte):

    page_title = 'Análise de Dados'

    nav_name = 'analyze'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'analytics/home/index.html', context)


@login_required()
def balance(request):

    page_title = 'Análise de Dados'

    nav_name = 'analyze'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }

    return render(request, 'analytics/home/index.html', context)
