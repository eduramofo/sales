import vobject
from leads.models import Lead
from account.models import Account


def gerar_leads(form, request):
    referrer = form.save()
    account = Account.objects.get(user=request.user)
    referrer.account = account
    account.save()
    files = request.FILES.getlist('vcf_files')
    contacts = handle_uploaded_files(files)
    create_leads_by_contacts(account, contacts, referrer)
    return referrer


def handle_uploaded_files(request_files):
    contacts = []
    for contacts_files in request_files:
        contacts = contacts + process_contacts_file(contacts_files.file)
    return contacts


def create_leads_by_contacts(account, contacts, referrer):
    leads = []
    for contact in contacts:
        new_lead = create_or_get_lead(account, contact, referrer)
        leads.append(new_lead)
    referrer.leads.set(leads)
    referrer.save()


def create_or_get_lead(account, contact, referrer):
    tels = contact['tels']
    tels_len = len(tels)
    tel = contact['tels'][0]['numero']
    waid = contact['tels'][0]['waid']
    name = contact['nome']
    note = ''

    if tels_len > 1:
        for current_tel in tels:
            current_tel_numero =  current_tel['numero']
            current_tel_waid = current_tel['waid']

            if current_tel_numero and current_tel_numero != 'NN' and current_tel_waid and current_tel_waid != 'NN':
                tel = current_tel_numero
                waid = current_tel_waid

            else:
                if current_tel_numero and current_tel_numero != 'NN' and current_tel_waid and current_tel_waid != 'NN':
                    note = note + '[ Tel: {}, Whats: https://wa.me/{} ]\n'.format(current_tel_numero, current_tel_waid)

                elif current_tel_numero and current_tel_numero != 'NN':
                    note = note + '[ Tel: {} ]\n'.format(current_tel_numero, current_tel_waid)

                elif current_tel_waid and current_tel_waid != 'NN':
                    note = note + '[ Whats: https://wa.me/{} ]\n'.format(current_tel_numero, current_tel_waid)

    if waid == 'NN':
        new_lead = create_lead(name, tel, waid, referrer.gmt, referrer.location, referrer.short_description, note, referrer.account)

    if waid != 'NN':
        lead = Lead.objects.filter(account=account, waid=waid).first()
        if lead is None:
            new_lead = create_lead(name, tel, waid, referrer.gmt, referrer.location, referrer.short_description, note, referrer.account)
        else:
            new_lead = lead

    return new_lead


def create_lead(name, tel, waid, gmt, location, short_description, note, account):
    new_created_lead = Lead.objects.create(
        name=name,
        nickname=name,
        tel=tel,
        waid=waid,
        gmt=gmt,
        location=location,
        short_description=short_description,
        note=note,
        account=account,
    )
    return new_created_lead


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
    contact = {
        'nome': nome,
        'tels': tels,
    }
    return contact


def get_vcard_tels_from_contents(contents):
    tels = []
    if 'tel' in contents:
        for tel in contents['tel']:
            tel_obj = process_tel_if_exist(tel)
            tels.append(tel_obj)
    else:
        current_tel_obj = {'numero': 'NN', 'waid': 'NN'}
        tels.append(current_tel_obj)
    return tels


def process_tel_if_exist(tel):
    current_numero = tel.value
    if current_numero == '':
        current_numero == 'NN'
    current_waid = 'NN' 
    if 'WAID' in tel.params.keys():
        current_waid = tel.params['WAID'][0]
    current_tel_obj = {'numero': current_numero, 'waid': current_waid}
    return current_tel_obj
