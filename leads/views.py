from urllib.parse import urlencode

from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages

from leads.process_contacts import gerar_leads
from leads.models import Lead
from leads.forms import LeadForm, UploadContactsForm
from leads.indicators import indicators_data
from leads.filters import LeadFilter


@login_required()
def leads_list(request):
    
    nav_name = 'leads_list'

    page_title = 'Lista de Leads'
    
    leads = LeadFilter(request.GET, queryset=Lead.objects.all())

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': leads.qs,
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
            url = reverse_lazy('leads:go-to', args=(str(lead.id),))
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
    page_title = 'Atualização do Lead'
    nav_name = 'leads_list'
    method = request.method

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'lead': lead,
        'lead_form': lead_form,
    }

    if method == 'POST' and lead_form.is_valid():
        lead = lead_form.save()
        url = reverse_lazy('leads:go-to', args=(str(lead.id),))
        messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')
        return HttpResponseRedirect(url)

    if method == 'POST' and not lead_form.is_valid():
        messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário do lead!')
        context['lead_form'] = lead_form

    return render(request, 'leads/update/index.html', context)


@login_required()
def lead_go_to(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    page_title = 'Para onde você gostaria de encaminhado?'
    nav_name = 'leads_list'
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'lead': lead,
    }
    return render(request, 'leads/go_to/index.html', context)



@login_required()
def leads_novos_list(request):
    
    nav_name = 'leads_novos_list'

    page_title = 'Lista de Novos Leads'

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(status='novo').order_by('-quality'))

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': leads.qs,
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

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': leads.qs,
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def leads_agendamentos_list(request):
    
    nav_name = 'leads_agendamentos_list'

    page_title = 'Lista de Leads em Agendamentos'

    leads = Lead.objects.filter().order_by('next_contact')

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(
        status='agendamento'
    ).order_by('next_contact'))

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': leads.qs,
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

            gerar_leads(indicated_by, request.FILES)

            filter_querydict = {
                'indicated_by__exact': indicated_by,
            }
            
            lead_admin_changelist_url = reverse('admin:leads_lead_changelist')

            success_url = '%s?%s' % (lead_admin_changelist_url, urlencode(filter_querydict))

            return HttpResponseRedirect(success_url)

    context = {
        'nav_name': 'leads_upload',
        'upload_contacts_form': upload_contacts_form
    }

    return render(request, 'leads/upload/index.html', context)
