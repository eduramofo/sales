from django.db.models import F
from django.utils import timezone

from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from leads.process_contacts import gerar_leads
from leads.forms import ReferrerForm
from leads import tools
from leads import models as leads_models
from leads.indicators import indicators_data

from core.tools import paginator


@login_required()
def referrers(request):

    referrers = leads_models.Referrer.objects.all().order_by(
        F('referring_datetime').desc(nulls_last=True)
    )


    nav_name = 'leads_referrers'
    
    page_title = 'Referenciadores'

    context = {
        'nav_name': nav_name,
        'page_title': page_title,
        'referrers': referrers,
    }

    return render(request, 'leads/referrers/list/index.html', context)


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
            return HttpResponseRedirect(reverse('leads:leads_referrers_all', args=[str(referrer.id),]))
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

