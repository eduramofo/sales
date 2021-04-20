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


@login_required()
def update(request):
    context = {}
    return render(request, 'leads/update_v2/index.html', context)


@login_required()
def update_content(request, lead_id):

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

    return render(request, 'leads/update_v2/content.html', context)
