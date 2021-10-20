from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms import formset_factory
from core.tools import paginator
from leads.models import Lead, Referrer
from leads.forms import LeadSimpleForm
from leads.filters import LeadFilter
from leads.forms import ReferrerForm


@login_required()
def t1(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.t1())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "T1" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def t2(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.t2())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "T2" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def t3(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.t3())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "T3" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def ghosting_1(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.ghosting_1())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Bolo 1" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def ghosting_2(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.ghosting_2())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Bolo 2" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def lna(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.lna())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Não atenderam" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def events(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.events())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Eventos" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def lost(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.lost())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Perdidos" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def ultimatum(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.ultimatum())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Ultimato" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def off_1(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.off_1())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Off 1" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def off_2(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.off_2())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Off 2" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def invalid(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.invalid())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Inválidos" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)

@login_required()
def win(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.win())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Ganhos" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def all(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    leads = LeadFilter(request.GET, queryset=referrer_obj.all())
    pages = paginator.make_paginator(request, leads.qs, 50)
    page_title = 'Leads "Todos" do(a) {}'.format(referrer_obj)
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'leads': pages['page'],
        'page_range': pages['page_range'],
        'leads_filters_form': leads.form,
    }
    return render(request, 'leads/list/index.html', context)


@login_required()
def edit_leads(request, referrer_id):

    nav_name = 'leads_list'

    referrer_obj = get_object_or_404(Referrer, id=referrer_id)

    leads = referrer_obj.leads.order_by('-priority', 'name')

    page_title = 'Editar Leads do(a) {}'.format(referrer_obj)

    LeadSimpleFormset = formset_factory(LeadSimpleForm, extra=0)

    if request.method == 'POST':
        lead_simple_formset = LeadSimpleFormset(request.POST)
        if lead_simple_formset.is_valid():
            for lead_data in lead_simple_formset.cleaned_data:
                lead_obj = get_object_or_404(Lead, id=lead_data['lead_id'])
                lead_obj.status = lead_data['status']
                lead_obj.name = lead_data['name']
                lead_obj.nickname = lead_data['nickname']
                lead_obj.gender = lead_data['gender']
                lead_obj.priority = lead_data['priority']
                lead_obj.tel = lead_data['tel']
                lead_obj.waid = lead_data['waid']
                lead_obj.note = lead_data['note']
                lead_obj.location = lead_data['location']
                lead_obj.gmt = lead_data['gmt']
                lead_obj.save()
        message_text = 'Leads atualizados com sucesso!'
        messages.add_message(request, messages.SUCCESS, message_text)
        success_url = reverse('leads:referrer_actions:edit_leads', args=[str(referrer_obj.id)])
        return HttpResponseRedirect(success_url)

    else:
        lead_simple_formset_initial = []
        for lead in leads:
            lead_simple_formset_initial.append(
                {
                    'lead_id': lead.id,
                    'status': lead.status,
                    'gender': lead.gender,
                    'priority': lead.priority,
                    'tel': lead.tel,
                    'waid': lead.waid,
                    'note': lead.note,
                    'name': lead.name,
                    'location': lead.location,
                    'gmt': lead.gmt,
                    'nickname': lead.nickname,
                }
            )
        lead_simple_formset = LeadSimpleFormset(initial=lead_simple_formset_initial)

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'formset': lead_simple_formset,
        'referrer': referrer_obj,
    }

    return render(request, 'leads/referrers/list_edit/index.html', context)


@login_required()
def update_card(request, referrer_id):
    nav_name = 'leads_list'
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    page_title = 'Editar cartão dos leads do(a) {}'.format(referrer_obj)
    form = ReferrerForm(instance=referrer_obj)
    method = request.method
    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'form': form,
        'referrer': referrer_obj,
    }
    if method == 'POST':
        form = ReferrerForm(request.POST, instance=referrer_obj)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cartão de indicação atualizado com sucesso!')
            redirect_url = reverse_lazy('leads:referrer_actions:edit_card', args=(str(referrer_obj.id),))
            return HttpResponseRedirect(redirect_url)
        else:
            messages.add_message(request, messages.ERROR, 'Existem erros no formulário, faça as devidas correções!')
            context['form'] = form
    return render(request, 'leads/referrers/update_card/index.html', context)


@login_required()
def next(request, referrer_id):
    referrer_obj = get_object_or_404(Referrer, id=referrer_id)
    lead = referrer_obj.next()
    if lead is not None:
        redirect_url = reverse_lazy('leads:update', args=(str(lead.id),))
    else:
        redirect_url = reverse_lazy('leads:referrer_actions:all', args=(str(referrer_obj.id),))
    return HttpResponseRedirect(redirect_url)
