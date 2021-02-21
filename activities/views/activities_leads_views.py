from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone

from core.tools import paginator

from activities.models import Activity
from activities.forms import ActivityForm
from activities.filters import ActivityFilter

from leads import models as LeadsModels


@login_required()
def add_through_lead(request, lead_id):

    shortcut = request.GET.get('shortcut', None)

    lead = get_object_or_404(LeadsModels.Lead, id=lead_id)

    lead_update_url = reverse_lazy('leads:update', args=(str(lead.id),))

    prefix_activity_form = 'activity_add_through_lead'

    due_date = timezone.localtime(timezone.now()).strftime('%Y-%m-%dT%H:%M')

    subject = None

    type_ = 'call'

    initial_activity_done = True

    if shortcut == 't1':
        subject = 'Não atendeu'
        Activity.objects.create(lead=lead, due_date=timezone.now(), done=True, subject=subject, type=type_)
        lead_status = lead.status
        if lead_status == 'novo' or lead_status == 'tentando_contato' or lead_status == 'tentando_contato_2':
            lead.status = 'tentando_contato'
            lead.save()
        messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendeu.')
        return HttpResponseRedirect(lead_update_url)

    if shortcut == 't2':
        subject = 'Não atendeu'
        Activity.objects.create(lead=lead, due_date=timezone.now(), done=True, subject=subject, type=type_)
        lead_status = lead.status
        if lead_status == 'novo' or lead_status == 'tentando_contato' or lead_status == 'tentando_contato_2':
            lead.status = 'tentando_contato_2'
            lead.save()
        messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendeu.')
        return HttpResponseRedirect(lead_update_url)

    if shortcut == 't3':
        subject = 'Não atendeu'
        Activity.objects.create(lead=lead, due_date=timezone.now(), done=True, subject=subject, type=type_)
        lead_status = lead.status
        if lead_status == 'novo' or lead_status == 'tentando_contato' or lead_status == 'tentando_contato_2':
            lead.status = 'geladeira'
            lead.save()
        messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendeu.')
        return HttpResponseRedirect(lead_update_url)

    if shortcut == 'sem-interesse':
        subject = 'Sem interesse'
        Activity.objects.create(lead=lead, due_date=timezone.now(), done=True, subject=subject, type=type_)
        lead.status = 'sem_interesse'
        lead.save()
        messages.add_message(request, messages.SUCCESS, 'Marcado como sem interesse.')
        return HttpResponseRedirect(lead_update_url)

    if shortcut == 'sem-dinheiro':
        subject = 'Sem condições financeiras'
        Activity.objects.create(lead=lead, due_date=timezone.now(), done=True, subject=subject, type=type_)
        lead.status = 'sem_condicoes_financeiras'
        lead.save()
        messages.add_message(request, messages.SUCCESS, 'Marcado como sem dinheiro.')
        return HttpResponseRedirect(lead_update_url)

    if shortcut == 'contato-invalido':
        subject = 'Contato Inválido'
        Activity.objects.create(lead=lead, due_date=timezone.now(), done=True, subject=subject, type=type_)
        lead.status = 'contato_invalido'
        lead.save()
        messages.add_message(request, messages.SUCCESS, 'Marcado como inválido.')
        return HttpResponseRedirect(lead_update_url)

    if shortcut == 'agendamento':
        subject = 'Agendamento'
        lead.status = 'agendamento'
        initial_activity_done = False
        lead.save()

    if shortcut == 'apresentacao-ganha':
        subject = 'Apresentação realizada ganha'
        lead.status = 'ganho'
        lead.save()

    if shortcut == 'apresentacao-perdida':
        subject = 'Apresentação realizada perdida'
        lead.status = 'perdido'
        lead.save()

    if shortcut == 'follow-up':
        subject = 'Acompanhamento'
        lead.status = 'acompanhamento'
        lead.save()

    initial_activity_initial = {
        'lead': str(lead.id),
        'due_date': due_date,
        'done': initial_activity_done,
        'subject': subject,
        'type': type_,
    }

    activity_form = ActivityForm(
        initial=initial_activity_initial,
        prefix=prefix_activity_form,
    )

    page_title = 'Criação de atividade para o Lead {}'.format(lead)

    nav_name = 'activities'

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'activity_form': activity_form,
        'lead': lead,
    }

    if request.method == 'POST':
        activity_form = ActivityForm(request.POST, prefix=prefix_activity_form)
        if activity_form.is_valid():
            activity = activity_form.save()            
            messages.add_message(request, messages.SUCCESS, 'Atividade criada com sucesso!')
            return HttpResponseRedirect(lead_update_url)
        else:
            messages.add_message(request, messages.ERROR, 'Há erro(s) no formulário de atividade.')
            context['activity_form'] = activity_form

    return render(request, 'activities/leads/add_through_lead/index.html', context)


@login_required()
def update_through_lead(request, activity_id):

    activity = get_object_or_404(Activity, id=activity_id)
    
    activity_form = ActivityForm(request.POST or None, instance=activity, prefix='activity')
    
    page_title = 'Atualização de Atividade | LEAD: {}'.format(activity.lead)
    
    nav_name = 'activities'

    method = request.method

    context = {
        'page_title': page_title,
        'nav_name': nav_name,
        'activity': activity,
        'activity_form': activity_form,
    }

    if method == 'POST':
        if activity_form.is_valid():
            activity = activity_form.save()
            url = reverse_lazy('leads:update', args=(str(activity.lead.id),))
            messages.add_message(request, messages.SUCCESS, 'Atividade atualizado com sucesso!')
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, 'Dados incorretos preenchido no formulário da atividade!')

    return render(request, 'activities/leads/update_through_lead/index.html', context)
