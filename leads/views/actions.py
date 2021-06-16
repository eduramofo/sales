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
from leads.models import Lead, Qualified, WhatsappTemplate
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
def off(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
        
    lead.status = 'off'

    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Off',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def lost_direct(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)

    lead.status = 'perdido'

    status_lost_justification = 'lost_direct'

    lead.status_lost_justification = status_lost_justification

    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Perdido Direto (Mensagem etc)',
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


@login_required()
def jump(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)

    lead.order = lead.order + 1

    lead.save()

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def ultimatum(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'ultimatum'

    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Ultimato',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def invalid(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'invalid'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Inválido',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def ghosting(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'ghosting'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Bolo 1',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def ghosting_2(request, lead_id):

    lead = get_object_or_404(Lead, id=lead_id)
    
    lead.status = 'ghosting_2'
    
    lead.save()

    Activity.objects.create(
        lead=lead,
        due_date=timezone.now(),
        done=True,
        subject='Bolo 2',
        type='call'
    )

    messages.add_message(request, messages.SUCCESS, 'Lead atualizado com sucesso!')

    url = reverse_lazy('leads:update', args=(str(lead.id),))

    return HttpResponseRedirect(url)


@login_required()
def upload(request, lead_id):
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

    return render(request, 'leads/actions/upload/index.html', context)


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
    activity_object = get_object_or_404(Activity, id=activity_id).delete()
    url = reverse_lazy('leads:update', args=(lead_id,))
    messages.add_message(request, messages.SUCCESS, 'Atividade excluída com sucesso!')
    return HttpResponseRedirect(url)
