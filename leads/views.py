from urllib.parse import urlencode
from django.shortcuts import render, HttpResponseRedirect, reverse
from leads.forms import UploadContactsForm
from leads.process_contacts import gerar_leads
from django.contrib.auth.decorators import login_required
from leads.models import Lead
from django.db.models import Q


@login_required()
def leads_list(request):
    
    leads = []

    leads_status = request.GET.get('status', None)
    
    if leads_status:
        leads = Lead.objects.filter(status=leads_status).order_by('next_contact').order_by('next_contact')
    else:
        leads = Lead.objects.filter(Q(status='novo') | Q(status='tentando_contato') | Q(status='processando')).order_by('-quality')
    
    context = {
        'nav_name': 'leads_list',
        'leads': leads,
    }

    return render(request, 'leads/list//index.html', context)


@login_required()
def leads_upload(request):

    upload_contacts_form = UploadContactsForm()

    if request.method == 'POST':

        upload_contacts_form = UploadContactsForm(request.POST)   

        if upload_contacts_form.is_valid():

            upload_contacts_form_data = upload_contacts_form.cleaned_data

            indicated_by = upload_contacts_form_data['indicated_by']

            gerar_leads(indicated_by, request.FILES)

            filter_querydict = {
                'indicated_by__exact': indicated_by,
            }
            
            lead_admin_changelist_url = reverse('admin:leads_lead_changelist')

            success_url = '%s?%s' % (lead_admin_changelist_url, urlencode(filter_querydict))

            return HttpResponseRedirect(success_url)

    context = {
        'nav_name': 'leads_upload',
        'upload_contacts_form': upload_contacts_form
    }

    return render(request, 'leads/upload/index.html', context)
