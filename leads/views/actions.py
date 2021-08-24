from random import choice as random_choice

from django.conf import settings
from django.utils import timezone
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib import messages

from activities.models import Activity
from conversation.models import Conversation
from event.create_from_lead import create_event
from leads.process_contacts import gerar_leads
from leads.models import Lead,  WhatsappTemplate
from leads.forms import ReferrerForm, ScheduleForm
from leads import tools
from leads.whatsapp import api as whatsapp_api
from account.models import Account


# contact attempt
@login_required()
def t1(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'tentando_contato'
    
    lead.save()

    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Não atendeu T1',
        type='call',
    )

    messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendida.')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def t2(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'tentando_contato_2'
    
    lead.save()

    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Não atendeu T2',
        type='call',
    )

    messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendida.')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def t3(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'geladeira'
    
    lead.save()

    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Não atendeu T3',
        type='call',
    )

    messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendida.')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def lost_direct(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)

    lead.status = 'perdido'

    status_lost_justification = 'lost_direct'

    lead.status_lost_justification = status_lost_justification

    lead.save()

    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        account=account,
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Perdido direto (mensagem etc)',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def ultimatum(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'ultimatum'

    lead.save()
    
    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        account=account,
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Ultimato',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def jump(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)

    lead.order = lead.order + 1

    lead.save()

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def invalid(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'invalid'
    
    lead.save()
    
    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Inválido',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def ghosting(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'ghosting'
    
    lead.save()

    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Bolo 1',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def ghosting_2(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    lead.status = 'ghosting_2'
    lead.save()
    account = Account.objects.get(user=request.user)
    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Bolo 2',
        type='call'
    )
    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')
    url = reverse_lazy('leads:update', args=(str(lead.id),))
    return HttpResponseRedirect(url)


# contact attempt
@login_required()
def schedule_direct(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    schedule_form = ScheduleForm()
    context = {
        'schedule_form': schedule_form,
        'lead': lead,
        'activity': None,
        'whatsapp_confirm': None,
    }
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST or None)
        context['schedule_form'] = schedule_form
        if schedule_form.is_valid():
            return create_event(request, False, context, lead, schedule_form)
        else:
            context['schedule_form'] = schedule_form
    return render(request, 'leads/update/schedule/entry.html', context)


# contact attempt
@login_required()
def schedule(request, lead_id):
    
    lead = get_object_or_404(Lead, id=lead_id)
    
    schedule_form = ScheduleForm()

    context = {
        'schedule_form': schedule_form,
        'lead': lead,
        'activity': None,
        'whatsapp_confirm': None,
    }

    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST or None)
        context['schedule_form'] = schedule_form
        if schedule_form.is_valid():
            return create_event(request, True, context, lead, schedule_form)

    return render(request, 'leads/update/schedule/entry.html', context)


# conversation
@login_required()
def lost(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    status_lost_justification = request.GET.get('justification', None)
    
    lead.status = 'perdido'
    
    lead.status_lost_justification = status_lost_justification

    lead.save()

    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Perdido',
        type='call'
    )

    if status_lost_justification == 'entrevista_perdida':
        Conversation.objects.create(lead=lead, account=account, type=Conversation.CONVERSATION_LOST)
    
    elif status_lost_justification == 'di':
        Conversation.objects.create(lead=lead, account=account, type=Conversation.CONVERSATION_DI)
    
    elif status_lost_justification == 'sem_interesse':
        Conversation.objects.create(lead=lead, account=account, type=Conversation.CONVERSATION_SEM_INTERESSE)

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# conversation
@login_required()
def off(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
        
    lead.status = 'off'

    lead.save()

    account = Account.objects.get(user=request.user)

    Activity.objects.create(
        lead=lead,
        account=account,
        due_date=timezone.now(),
        done=True,
        subject='Off',
        type='call'
    )

    Conversation.objects.create(lead=lead, account=account, type=Conversation.CONVERSATION_OFF)

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# conversation
@login_required()
def win(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'ganho'
    
    lead.save()
    
    account = Account.objects.get(user=request.user)

    Activity.objects.create(lead=lead, account=account, due_date=timezone.now(), done=True, subject='Ganho', type='call')

    Conversation.objects.create(lead=lead, account=account, type=Conversation.CONVERSATION_WIN)

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


# next
@login_required()
def next(request):
    random_queryset_list =  tools.get_open_run_now_leads()
    if not random_queryset_list:
        random_queryset_list = tools.get_open_leads()
    pks = random_queryset_list.values_list('pk', flat=True)
    random_pk = random_choice(pks)
    next_lead_url = reverse('leads:update', args=[random_pk,])
    return HttpResponseRedirect(next_lead_url)


@login_required()
def add(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    indicated_by_datetime = timezone.localtime(timezone.now()).strftime('%Y-%m-%dT%H:%M')
    gmt = -3
    initial = {
        'name': str(lead),
        'lead': str(lead.id),
        'referring_datetime': indicated_by_datetime,
        'gmt': gmt,
    }
    form = ReferrerForm()
    form = ReferrerForm(initial=initial)

    if request.method == 'POST':
        form = ReferrerForm(request.POST)
        if form.is_valid():
            referrer = gerar_leads(form, request)
            message_text = 'Leads criados com sucesso =)'
            messages.add_message(request,messages.SUCCESS, message_text)
            return HttpResponseRedirect(reverse('leads:leads_referrers_edit', args=[str(referrer.id),]))
        else:
            message_text = 'Ocorreu um ERRO durante a inclusão dos Leads, faça uma verificação manual!'
            messages.add_message(request,messages.ERROR, message_text)

    page_title = 'Upload de Contatos para ' + str(lead)

    context = {
        'nav_name': 'leads_upload',
        'page_title': page_title,
        'form': form,
        'lead': lead,
    }

    return render(request, 'leads/actions/add/index.html', context)


@login_required()
def add_upload(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    indicated_by_datetime = timezone.localtime(timezone.now()).strftime('%Y-%m-%dT%H:%M')
    gmt = -3
    initial = {
        'name': str(lead),
        'lead': str(lead.id),
        'referring_datetime': indicated_by_datetime,
        'gmt': gmt,
    }
    form = ReferrerForm()
    form = ReferrerForm(initial=initial)

    if request.method == 'POST':
        form = ReferrerForm(request.POST)
        if form.is_valid():
            referrer = gerar_leads(form, request)
            message_text = 'Leads criados com sucesso =)'
            messages.add_message(request,messages.SUCCESS, message_text)
            return HttpResponseRedirect(reverse('leads:leads_referrers_edit', args=[str(referrer.id),]))
        else:
            message_text = 'Ocorreu um ERRO durante a inclusão dos Leads, faça uma verificação manual!'
            messages.add_message(request,messages.ERROR, message_text)

    page_title = 'Upload de Contatos para ' + str(lead)

    context = {
        'nav_name': 'leads_upload',
        'page_title': page_title,
        'form': form,
        'lead': lead,
    }

    return render(request, 'leads/actions/add/upload/index.html', context)


@login_required()
def whatsapp_template(request, lead_id, whatsapp_template_id):
    lead = get_object_or_404(Lead, id=lead_id)
    whatsapp_template_object = get_object_or_404(WhatsappTemplate, id=whatsapp_template_id)
    first_name = request.user.first_name
    waid = lead.waid
    url = whatsapp_api.make_whastapp_api_link(waid, whatsapp_template_object, lead, first_name)
    return HttpResponseRedirect(url)


@login_required()
def activity_delete(request, lead_id, activity_id):
    activity_object = get_object_or_404(Activity, id=activity_id)
    activity_object.delete()
    url = reverse_lazy('leads:update', args=(lead_id,))
    messages.add_message(request, messages.SUCCESS, 'Atividade excluída com sucesso!')
    return HttpResponseRedirect(url)
