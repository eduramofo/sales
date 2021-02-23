from urllib.parse import urlencode
from random import choice as random_choice

from django.utils import timezone
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages

from core.tools import paginator

from activities.models import Activity

from leads.process_contacts import gerar_leads
from leads.models import Lead, Qualified
from leads.forms import LeadForm, LeadLostForm, LeadFormRunNow, ReferrerForm, QualifiedForm
from leads.filters import LeadFilter
from leads import tools
from leads.templatetags import leads_extras



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
def lead_update_lost(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    lead_lost_form = LeadLostForm(request.POST or None, instance=lead)
    page_title = 'Confirmação da perda do Lead: ' + str(lead.name)
    nav_name = 'leads_list'
    method = request.method

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'lead': lead,
        'lead_lost_form': lead_lost_form,
    }

    if method == 'POST':
        if lead_lost_form.is_valid():
            lead = lead_lost_form.save()
            lead.status = 'perdido'
            lead.save()
            url = reverse_lazy('leads:update', args=(str(lead.id),))
            messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário do lead!')
            context['lead_lost_form'] = lead_lost_form

    return render(request, 'leads/lost/index.html', context)


@login_required()
def lead_update_win(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    lead_form = LeadForm(request.POST or None, instance=lead)
    activities = Activity.objects.filter(lead=lead).order_by('-created_at')
    page_title = str(lead.name)
    nav_name = 'leads_list'
    method = request.method
    
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'lead': lead,
        'activities': activities,
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
def lead_next_referrer(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    # next_lead = tools.get_referrers_next_lead(lead)
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
