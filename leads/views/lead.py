from urllib.parse import urlencode
from random import choice as random_choice

from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages

from core.tools import paginator

from activities.models import Activity

from leads.process_contacts import gerar_leads
from leads.models import Lead, Qualified
from leads.forms import LeadForm, QualifiedForm
from leads.filters import LeadFilter
from leads import tools
from leads.templatetags import leads_extras



@login_required()
def lead_add(request):

    initial = {}
    
    lead_form = LeadForm(
        initial=initial
    )

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
    activities = Activity.objects.filter(lead=lead).order_by('-created_at')
    page_title = "{} ({})".format(lead.name, lead.get_status_display())
    nav_name = 'leads_list'
    method = request.method
    referrers = leads_extras.get_referrers_from_lead(lead)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'lead': lead,
        'activities': activities,
        'referrers': referrers,
        'lead_form': lead_form,
    }

    if method == 'POST':
        if lead_form.is_valid():
            lead = lead_form.save()
            go_next = request.GET.get('next', None)
            url = reverse_lazy('leads:update', args=(str(lead.id),))
            if go_next:
                url = reverse_lazy('leads:next')
            messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário do lead!')
            context['lead_form'] = lead_form

    return render(request, 'leads/update/index.html', context)


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
def lead_next_referrer(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    next_lead_id = tools.get_referrers_next_lead(lead)
    next_lead_url = reverse('leads:update', args=[next_lead_id,])
    return HttpResponseRedirect(next_lead_url)


@login_required()
def leads_list(request):
    
    nav_name = 'leads_list'

    page_title = 'Lista de Leads'
    
    leads = LeadFilter(request.GET, queryset=Lead.objects.all().order_by('-created_at'))

    pages = paginator.make_paginator(request, leads.qs, 9)

    context = {
        'page_title': page_title,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'nav_name': nav_name,
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


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
def leads_news(request):
    
    nav_name = 'leads_news'

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
def leads_opened(request):
    
    nav_name = 'leads_opened'

    page_title = 'Lista de Leads em Aberto'

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(
        Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')
    ).order_by('-quality'))

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def leads_priorities(request):
    
    nav_name = 'leads_priorities'

    page_title = 'Leads prioritários em aberto'

    query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')

    leads = LeadFilter(request.GET, queryset=Lead.objects.filter(priority=True).filter(query))

    pages = paginator.make_paginator(request, leads.qs, 30)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }

    return render(request, 'leads/list/index.html', context)


@login_required()
def leads_schedules(request):
    
    nav_name = 'leads_schedules'

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


def qualified(request):

    initial = {}

    form = QualifiedForm(initial=initial)

    context = {
        'page_title': 'Aprenda Inglês Online!',
        'form': form,
    }

    if request.method == 'POST':
        form = QualifiedForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            waid = form.cleaned_data['waid']
            qualified = Qualified.objects.create(name=name, waid=waid,)
            url = reverse_lazy('core:qualified_confirmed', args=(str(qualified.id),))
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Existem dados incorretos preenchido no formulário!')
            context['form'] = form

    return render(request, 'leads/qualified/add/index.html', context)


def qualified_confirmed(request, qualified_id):

    qualified = get_object_or_404(Qualified, id=qualified_id)

    context = {
        'page_title': 'Aprenda Inglês Online!',
        'qualified': qualified,
    }

    return render(request, 'leads/qualified/confirmed/index.html', context)


def speech_start(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)

    lead_first_name = lead.name.partition(' ')[0]
    
    referrer_name = lead.get_referrer_name()

    context = {
        'page_title': 'Escolha o Speech',
        'lead': lead,
        'lead_first_name': lead_first_name,
        'referrer_name': referrer_name,
    }

    return render(request, 'leads/speech/start/index.html', context)


def speech_show(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)

    lead_first_name = lead.name.partition(' ')[0]

    lead_gender = request.GET.get('l', None)

    referrer_name = lead.get_referrer_name()

    referrer_gender = request.GET.get('r', None)

    referrer_win = request.GET.get('rm', None)

    context = {

        'page_title': 'Modelo de Speech ({} - {})'.format(referrer_name, lead_first_name),

        'lead': lead,
        'lead_first_name': lead_first_name,
        'lead_gender': lead_gender,

        'referrer_name': referrer_name,
        'referrer_gender': referrer_gender,
        'referrer_win': referrer_win,
    }

    return render(request, 'leads/speech/index.html', context)
