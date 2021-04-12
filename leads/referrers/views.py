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
def t2(request, lead_id):

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
def t3(request, lead_id):

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
def schedule(request, lead_id):

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