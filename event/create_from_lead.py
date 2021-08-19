import datetime
from activities.models import Activity
from conversation.models import Conversation
from account.models import Account
from event.models import Event
from leads.whatsapp import api as whatsapp_api
from django.contrib import messages
from django.shortcuts import render


def create_event(request, had_a_conversation, context, lead, form):
    form = form.cleaned_data
    start_datetime = form['due_date']
    account = Account.objects.get(user=request.user)
    duration_in_minutes = 35
    end_datetime = start_datetime + datetime.timedelta(minutes=duration_in_minutes)
    event_obj = Event.objects.create(
        account=account,
        summary='WSP - ' + str(lead),
        lead=lead,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        done=False,
    )
    event_obj_start_datetime = event_obj.start_datetime.strftime('%d/%m/%y às %H:%M')
    first_name = request.user.first_name
    whatsapp_confirm = whatsapp_api.schedule_due_date(lead, first_name, 'agendamento_confirmacao_auto', event_obj_start_datetime)
    context['whatsapp_confirm'] = whatsapp_confirm
    context['event'] = event_obj
    if had_a_conversation:
        lead.status = 'agendamento'
    else:
        lead.status = 'agendamento_direct'
    lead.save()
    Activity.objects.create(lead=lead, account=account, due_date=start_datetime, done=False, subject='Agendamento criado', type='call')
    if had_a_conversation:
        Conversation.objects.create(lead=lead, account=account, type=Conversation.CONVERSATION_AGENDAMENTO)
    messages.add_message(request, messages.SUCCESS, 'Agendamento criado com sucesso!')
    return render(request, 'leads/update/schedule/success_event.html', context)
