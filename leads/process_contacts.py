from django.conf import settings
from leads.models import Lead
import vobject
import json


def gerar_leads(form, request):
    referrer = form.save()
    files = request.FILES.getlist('vcf_files')
    contacts = handle_uploaded_files(files)
    create_leads_by_contacts(contacts, referrer)


def create_leads_by_contacts(contacts, referrer):
    leads = []
    for contact in contacts:
        new_lead = Lead.objects.create(
            indicated_by=referrer.name,
            indicated_by_datetime=referrer.referring_datetime,
            name=contact['nome'],
            tel=contact['tels'][0]['numero'],
            waid=contact['tels'][0]['waid'],
            quality=1,
        )
        leads.append(new_lead)
    referrer.leads.set(leads)
    referrer.save()


def handle_uploaded_files(request_files):
    contacts = []
    for contacts_files in request_files:
        contacts = contacts + process_contacts_file(contacts_files.file)
    return contacts


def process_contacts_file(contacts_file):
    contacts = []
    source_file_readed = contacts_file.read().decode('utf-8')
    for vcard in vobject.readComponents(source_file_readed):
        contact = process_vcard(vcard)
        contacts.append(contact)
    return contacts


def process_vcard(vcard):
    nome = vcard.fn.value
    contents = vcard.contents
    tels = get_vcard_tels_from_contents(contents)
    contact = {'nome': nome, 'tels': tels,}
    return contact


def get_vcard_tels_from_contents(contents):
    tels = []
    if 'tel' in contents:
        for tel in contents['tel']:
            tel_obj = process_tel_if_exist(tel)
            tels.append(tel_obj)
    else:
        current_tel_obj = {'numero': 'SEM NUMERO', 'waid': 'SEM NUMERO'}
        tels.append(current_tel_obj)
    return tels


def process_tel_if_exist(tel):
    current_numero = tel.value
    current_waid = None 
    if 'WAID' in tel.params.keys():
        current_waid = tel.params['WAID'][0]
    current_tel_obj = {'numero': current_numero, 'waid': current_waid}
    return current_tel_obj
