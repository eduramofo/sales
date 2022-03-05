from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime, make_aware, now
from account.models import Account
from analytics import forms
from analytics import constants
from analytics.production import get_production_table
from analytics.balance import get_balance_table


@login_required()
def select(request):
    if request.method == 'POST':
        form = forms.RangeDateSelectForm(request.POST)
        if form.is_valid():        
            cleaned_data = form.cleaned_data  
            report = cleaned_data['report']
            date_format = '%Y-%m-%d'
            start_date = cleaned_data['start_date']
            end_date = cleaned_data['end_date']
            if report == constants.REPORT_PRODUCTION:
                return redirect('analytics:production', date_format=date_format, start_date=start_date, end_date=end_date)
            elif report == constants.REPORT_BALANCE:
                return redirect('analytics:balance', date_format=date_format, start_date=start_date, end_date=end_date)
            else:
                return redirect('analytics:production', date_format=date_format, start_date=start_date, end_date=end_date)
    else:
        today_str = now().today().strftime('%Y-%m-%d')
        select_range_date_form_initial = {
            'report': constants.REPORT_DEFAULT,
            'start_date': today_str,
            'end_date': today_str,
        }
        form = forms.RangeDateSelectForm(initial=select_range_date_form_initial)
    page_title = 'Selecione o Relatório e o Período'
    nav_name = 'analyze'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'form': form,
    }
    return render(request, 'analytics/select/index.html', context)


@login_required()
def production(request, date_format, start_date, end_date):    
    start_date_obj = make_aware(datetime.strptime(start_date, date_format))
    end_date_obj = make_aware(datetime.strptime(end_date, date_format))    
    account = Account.objects.get(user=request.user)
    page_title = 'Produtividade: {} ao {}'.format(start_date_obj.strftime('%d/%m/%Y'), end_date_obj.strftime('%d/%m/%Y'))
    nav_name = 'analyze'
    table = get_production_table(account, start_date_obj, end_date_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'table': table,
    }
    return render(request, 'analytics/production/index.html', context)


@login_required()
def balance(request, date_format, start_date, end_date):
    start_date_obj = make_aware(datetime.strptime(start_date, date_format))
    end_date_obj = make_aware(datetime.strptime(end_date, date_format))
    account = Account.objects.get(user=request.user)
    page_title = 'Balanço dos Leads: {} ao {}'.format(start_date_obj.strftime('%d/%m/%Y'), end_date_obj.strftime('%d/%m/%Y'))
    nav_name = 'analyze'
    table = get_balance_table(account, start_date_obj, end_date_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'table': table,
    }
    return render(request, 'analytics/balance/index.html', context)
