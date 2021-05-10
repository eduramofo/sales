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
from leads.forms import LeadForm, LeadLostForm, LeadFormRunNow, ReferrerForm, QualifiedForm, ScheduleForm
from leads.filters import LeadFilter
from leads import tools
from leads.templatetags import leads_extras
from leads.whatsapp import api as whatsapp_api


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
def t1(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'tentando_contato'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Não atendeu T1',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendida.')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def t2(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'tentando_contato_2'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Não atendeu T2',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendida.')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def t3(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'geladeira'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Não atendeu T3',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Ligação registrada como não atendida.')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


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
            schedule_form_cleaned_data = schedule_form.cleaned_data
            due_date = schedule_form_cleaned_data['due_date']
            lead.status = 'agendamento'
            lead.save()
            activity_obj = Activity.objects.create(
                lead=lead,
                due_date=due_date,
                done=False,
                subject='Agendamento criado',
                type='call'
            )
            activity_obj_due_date = activity_obj.due_date.strftime('%d/%m/%y às %H:%M')
            whatsapp_confirm = whatsapp_api.schedule_due_date(lead, 'Eduardo', 'agendamento_confirmacao_auto', activity_obj_due_date)
            context['whatsapp_confirm'] = whatsapp_confirm
            context['activity'] = activity_obj
            messages.add_message(request, messages.SUCCESS, 'Agendamento criado com sucesso!')
            return render(request, 'leads/update/schedule/success.html', context)
        else:
            context['schedule_form'] = schedule_form

    return render(request, 'leads/update/schedule/entry.html', context)


@login_required()
def upload(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'perdido'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Perdido',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def lost(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    status_lost_justification = request.GET.get('justification', None)
    
    lead.status = 'perdido'
    
    lead.status_lost_justification = status_lost_justification

    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Perdido',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def win(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'ganho'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Ganho',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)
