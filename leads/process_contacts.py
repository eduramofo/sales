from django.conf import settings
from leads.models import Lead
import vobject
import json


def gerar_leads(form, request):
    referrer = form.save()
    files = request.FILES.getlist('vcf_files')
    contacts = handle_uploaded_files(files)
    create_leads_by_contacts(contacts, referrer)
    return referrer


def create_leads_by_contacts(contacts, referrer):
    leads = []
    for contact in contacts:
        check_duplicate(contact, referrer)
        new_lead = create_lead(contact, referrer)
        leads.append(new_lead)
    referrer.leads.set(leads)
    referrer.save()


def create_lead(contact, referrer):
    tel = contact['tels'][0]['numero']
    waid = contact['tels'][0]['waid']
    name = contact['nome']
    
    new_lead = Lead.objects.create(
        name=name,
        tel=tel,
        waid=waid,
        gmt=referrer.gmt,
        location=referrer.location,
        short_description=referrer.short_description,
    )
    return new_lead


def check_duplicate(contact, referrer):
    pass


def handle_uploaded_files(request_files):
    contacts = []
    for contacts_files in request_files:
        contacts = contacts + process_contacts_file(contacts_files.file)
    return contacts


def process_contacts_file(contacts_file):
    contacts = []
    source_file_readed = contacts_file.read().decode('utf-8')
    source_file_readed = adjust_vcards_string(source_file_readed)
    vcards = vobject.readComponents(source_file_readed)
    for vcard in vcards:
        contact = process_vcard(vcard)
        contacts.append(contact)
    return contacts


def adjust_vcards_string(vcards_string):
    start, end = 'BEGIN:VCARD', 'END:VCARD'
    vcards_body = [item for item in (item.strip().strip(start) for item in vcards_string.split(end)) if item]
    new_vcards_string  = ''
    for card in vcards_body:
        new_vcards_string = new_vcards_string + '{}{}\n{}\n'.format(start, card, end)
    return new_vcards_string


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
