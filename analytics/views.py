from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.timezone import datetime, make_aware, timedelta

from activities.models import Activity
from account.models import Account
from analytics import day
from analytics import data_clean
from analytics import balance_data
from analytics import data
from analytics import forms


@login_required()
def home(request):
    page_title = 'Análise das Atividades'
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
    today = datetime.now()
    weekday = today.weekday()
    week_start = today - timedelta(days=weekday) + timedelta(days=2)
    if weekday == 1:
        week_start = today - timedelta(days=6)
    week_end = week_start + timedelta(days=6)
    week_start_str = week_start.strftime('%Y-%m-%d')
    week_end_str = week_end.strftime('%Y-%m-%d')
    args = (week_start_str, week_end_str)
    url = reverse_lazy('analytics:range_result', args=args)
    return HttpResponseRedirect(url)


@login_required()
def day_select(request):
    selected_day = request.GET.get('day', None)
    if selected_day:
        url = reverse_lazy('analytics:day_result', args=(selected_day,))
        return HttpResponseRedirect(url)
    day_select_form = forms.DaySelectForm()
    page_title = 'Selecione o Dia para Análise das Atividades'
    nav_name = 'analyze'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'form': day_select_form,
    }
    return render(request, 'analytics/day_select/index.html', context)


@login_required()
def day_result(request, dt):
    dt_obj = make_aware(datetime.strptime(dt, '%Y-%m-%d'))
    account = Account.objects.get(user=request.user)
    # DATA: START
    activities = data.get_activities_by_day(account, dt)
    conversations = data.get_conversations_by_day(account, dt)
    speechs = data.speechs_by_day(account, dt)
    win = data.win_by_day(account, dt)
    data_result = data_clean.data(activities, conversations, speechs, win)
    # DATA: END
    page_title = 'Análise das Atividades do Dia ' + dt_obj.strftime('%d/%m/%Y')
    nav_name = 'analyze'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'data': data_result,
    }
    return render(request, 'analytics/day_result/index.html', context)


@login_required()
def range_select(request):
    selected_day_start = request.GET.get('day-detail-date-start', None)
    selected_day_end = request.GET.get('day-detail-date-end', None)
    if selected_day_start and selected_day_end:
        args = (selected_day_start, selected_day_end)
        url = reverse_lazy('analytics:range_result', args=args)
        return HttpResponseRedirect(url)
    page_title = 'Selecione a Data Inicial e a Final para Análise das Atividades'
    nav_name = 'analyze'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
    }
    return render(request, 'analytics/range_select/index.html', context)


@login_required()
def range_result(request, dts, dte):
    gte_date = make_aware(datetime.strptime(dts, '%Y-%m-%d'))
    lte_date = make_aware(datetime.strptime(dte, '%Y-%m-%d'))
    activities = Activity.objects.filter(created_at__gte=gte_date, created_at__lte=lte_date).exclude(subject='Inválido')
    page_title = 'Análise das Atividades dos Dias Entre ({} e {})'.format(gte_date.strftime('%d/%m/%Y'), lte_date.strftime('%d/%m/%Y'))
    nav_name = 'analyze'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'data': day.get_data_clean(activities),
    }
    return render(request, 'analytics/range_result/index.html', context)


@login_required()
def balance(request):
    page_title = 'Balanço dos Leads'
    nav_name = 'analyze'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'data': balance_data.get_data(),
    }
    return render(request, 'analytics/balance/index.html', context)
