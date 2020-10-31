from urllib.parse import urlencode
from django.shortcuts import render, HttpResponseRedirect, reverse
from core.process_contacts import process_contacts_file
from leads.forms import UploadContactsForm
from leads.process_contacts import gerar_leads


def index(request):
    
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
        'upload_contacts_form': upload_contacts_form
    }

    return render(request, 'leads/index.html', context)
