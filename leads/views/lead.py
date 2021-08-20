from random import choice as random_choice
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from account.models import Account
from activities.models import Activity
from leads.models import Lead
from leads.forms import LeadForm
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
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead = lead_form.save()
            lead.account = account
            lead.save()
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
    account = Account.objects.get(user=request.user)
    if method == 'POST':
        if lead_form.is_valid():
            lead = lead_form.save()
            lead.account = account
            lead.save()
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
