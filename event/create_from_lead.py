import datetime
from activities.models import Activity
from conversation.models import Conversation
from event.models import Event
from leads.whatsapp import api as whatsapp_api
from django.contrib import messages
from django.shortcuts import render


def create_event(request, context, lead, form):
    form = form.cleaned_data
    start_datetime = form['due_date']
    duration_in_minutes = 35
    end_datetime = start_datetime + datetime.timedelta(minutes=duration_in_minutes)
    event_obj = Event.objects.create(
        summary='WSP - ' + str(lead),
        lead=lead,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        done=False,
    )
    event_obj_start_datetime = event_obj.start_datetime.strftime('%d/%m/%y às %H:%M')
    whatsapp_confirm = whatsapp_api.schedule_due_date(lead, 'Eduardo', 'agendamento_confirmacao_auto', event_obj_start_datetime)
    context['whatsapp_confirm'] = whatsapp_confirm
    context['event'] = event_obj
    lead.status = 'agendamento'
    lead.save()
    Conversation.objects.create(lead=lead, type=Conversation.CONVERSATION_AGENDAMENTO)
    messages.add_message(request, messages.SUCCESS, 'Agendamento criado com sucesso!')
    return render(request, 'leads/update/schedule/success_event.html', context)
