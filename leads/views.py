from urllib.parse import urlencode
from random import choice as random_choice

from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages

from core.tools import paginator

from activities.models import Activity

from leads.process_contacts import gerar_leads
from leads.models import Lead
from leads.forms import LeadForm, LeadFormRunNow, UploadContactsForm
from leads.indicators import indicators_data
from leads.filters import LeadFilter
from leads import tools
from leads.templatetags import leads_extras


@login_required()
def leads_list(request):
    
    nav_name = 'leads_list'

    page_title = 'Lista de Leads'
    
    leads = LeadFilter(request.GET, queryset=Lead.objects.all().order_by('-created_at'))

    pages = paginator.make_paginator(request, leads.qs, 10)

    context = {
        'page_title': page_title,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'nav_name': nav_name,
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def lead_add(request):

    initial = {}
    
    lead_form = LeadForm(initial=initial)

    page_title = 'Criação de um novo do Lead'

    nav_name = 'leads_list'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'lead_form': lead_form,
    }

    if request.method == 'POST':
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead = lead_form.save()
            url = reverse_lazy('leads:update', args=(str(lead.id),))
            messages.add_message(request, messages.SUCCESS, 'Lead adicionado com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário do lead!')
            context['lead_form'] = lead_form

    return render(request, 'leads/add/index.html', context)


@login_required()
def lead_update(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    lead_form = LeadForm(request.POST or None, instance=lead)
    activities = Activity.objects.filter(lead=lead)
    page_title = 'Atualização do Lead'
    nav_name = 'leads_list'
    method = request.method

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'lead': lead,
        'activities': activities,
        'lead_form': lead_form,
    }

    if method == 'POST' and lead_form.is_valid():
        lead = lead_form.save()
        go_next = request.GET.get('next', None)
        url = reverse_lazy('leads:update', args=(str(lead.id),))
        if go_next:
            url = reverse_lazy('leads:next')
        messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')
        return HttpResponseRedirect(url)

    if method == 'POST' and not lead_form.is_valid():
        messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário do lead!')
        context['lead_form'] = lead_form

    return render(request, 'leads/update/index.html', context)


@login_required()
def lead_update_run_now(request, lead_id, lead_run_now):

    lead = get_object_or_404(Lead, id=lead_id)
    lead_form_run_now = LeadFormRunNow(request.POST or None, instance=lead)
    method = request.method
    lead_run_now = lead_run_now.lower()
    run_now_status = None

    if lead_run_now == 'true':
        run_now_status = True

    elif lead_run_now == 'false':
        run_now_status = False

    response = {
        'success': False,
        'run_now': run_now_status,
        'td_html': '',
    }

    if method == 'POST':
        if lead_form_run_now.is_valid() and not run_now_status == None:
            lead = lead_form_run_now.save()
            lead_id = lead.id
            run_now = lead.run_now
            response['success'] = True
            response['run_now'] = run_now
            response['td_html'] =  leads_extras.run_now_table_data_html(lead_id, run_now),
            if run_now:         
                messages.add_message(request, messages.SUCCESS, 'Lead INCLUÍDO na lista de execução de AGORA com sucesso!')
            else:
                messages.add_message(request, messages.SUCCESS, 'Lead EXCLUÍDO na lista de execução de AGORA com sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu um ERRO durante a inclusão/excluído do Lead na lista de execução de agora!')

    return JsonResponse(response)


@login_required()
def lead_next(request):
    random_queryset_list =  tools.get_open_run_now_leads()
    if not random_queryset_list:
        random_queryset_list = tools.get_open_leads()
    pks = random_queryset_list.values_list('pk', flat=True)
    random_pk = random_choice(pks)
    next_lead_url = reverse('leads:update', args=[random_pk,])
    return HttpResponseRedirect(next_lead_url)


@login_required()
def leads_now(request):
    
    nav_name = 'leads_now'

    page_title = 'Lista de Leads [ AGORA ]'

    leads_queryset = tools.get_open_run_now_leads()

    leads = LeadFilter(request.GET, queryset=leads_queryset)

    pages = paginator.make_paginator(request, leads.qs, 10)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def leads_novos_list(request):
    
    nav_name = 'leads_novos_list'

    page_title = 'Lista de Novos Leads'

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(status='novo').order_by('-quality'))

    pages = paginator.make_paginator(request, leads.qs, 10)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def leads_em_aberto_list(request):
    
    nav_name = 'leads_em_aberto_list'

    page_title = 'Lista de Leads em Aberto'

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(
        Q(status='tentando_contato') | Q(status='processando')
    ).order_by('-quality'))
    
    pages = paginator.make_paginator(request, leads.qs, 10)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def leads_agendamentos_list(request):
    
    nav_name = 'leads_agendamentos_list'

    page_title = 'Lista de Leads em Agendamentos'

    leads = Lead.objects.filter().order_by('next_contact')

    leads = LeadFilter(
        request.GET, queryset=Lead.objects.filter(
            status='agendamento'
        ).order_by('next_contact')
    )

    pages = paginator.make_paginator(request, leads.qs, 10)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def leads_indicators_list(request):

    indicators = indicators_data()
    nav_name = 'leads_indicators_list'
    page_title = 'Lista Indicadores'
    
    context = {
        'nav_name': nav_name,
        'page_title': page_title,
        'indicators': indicators,
    }

    return render(request, 'leads/indicators_list/index.html', context)


@login_required()
def leads_upload(request):

    upload_contacts_form = UploadContactsForm()

    if request.method == 'POST':

        upload_contacts_form = UploadContactsForm(request.POST)   

        if upload_contacts_form.is_valid():

            upload_contacts_form_data = upload_contacts_form.cleaned_data

            indicated_by = upload_contacts_form_data['indicated_by']

            indicated_by_datetime = upload_contacts_form_data['indicated_by_datetime']

            gerar_leads(indicated_by, indicated_by_datetime, request.FILES)

            filter_querydict = {
                'indicated_by_contains': indicated_by,
            }
            
            filter_urlencode = urlencode(filter_querydict)

            leads_list = reverse('leads:list')
            
            success_url = '%s?%s' % (leads_list, filter_urlencode)

            messages.add_message(request, messages.SUCCESS, 'Leads criados SUCESSO!')
    
            return HttpResponseRedirect(success_url)
        
        else:

            messages.add_message(request, messages.ERROR, 'Ocorreu um ERRO durante a inclusão dos Lead, faça uma verificação manual!')


    context = {
        'nav_name': 'leads_upload',
        'upload_contacts_form': upload_contacts_form
    }

    return render(request, 'leads/upload/index.html', context)
