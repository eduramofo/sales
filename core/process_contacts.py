from django.conf import settings

import vobject
import json


def process_contacts_file(file_name):
    contacts_folder = settings.BASE_DIR / 'vcf'
    contacts_file = contacts_folder / file_name
    contacts = []
    with open(contacts_file, 'r') as source_file:
        for vcard in vobject.readComponents(source_file):
            tels = []
            for tel in vcard.contents['tel']:
                current_numero = tel.value
                current_waid = None 
                if 'WAID' in tel.params.keys():
                    current_waid = tel.params['WAID'][0]
                current_tel_obj = {'numero': current_numero, 'waid': current_waid}
                tels.append(current_tel_obj)
            contact = {
                'nome': vcard.fn.value,
                'tels': tels,
            }
            contacts.append(contact)
    return contacts
