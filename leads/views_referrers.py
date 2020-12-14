from django.utils import timezone
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from leads.process_contacts import gerar_leads
from leads.forms import ReferrerForm
from leads import tools
from leads import models as leads_models

from core.tools import paginator


@login_required()
def referrers(request):

    referrers = leads_models.Referrer.objects.all()

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

    indicated_by_datetime = timezone.now().strftime('%Y-%m-%dT%H:%M')

    gmt = -3

    form = ReferrerForm()

    initial = {
        'referring_datetime': indicated_by_datetime,
        'gmt': gmt,
    }

    form = ReferrerForm(initial=initial)

    if request.method == 'POST':
        form = ReferrerForm(request.POST)
        if form.is_valid():
            gerar_leads(form, request)
            message_text = 'Leads criados com sucesso =)'
            messages.add_message(request,messages.SUCCESS, message_text)
            return HttpResponseRedirect(reverse('leads:list'))
        else:
            message_text = 'Ocorreu um ERRO durante a inclusão dos Leads, faça uma verificação manual!'
            messages.add_message(request,messages.ERROR, message_text)

    context = {
        'nav_name': 'leads_upload',
        'form': form,
    }

    return render(request, 'leads/upload/index.html', context)
