from django.shortcuts import render
from core.process_contacts import process_contacts_file

import urllib.parse


def index(request):
    
    contacts1 = process_contacts_file('contatos_1.vcf')
    contacts2 = process_contacts_file('contatos_1.vcf')
    contacts3 = process_contacts_file('contatos_1.vcf')
    contacts4 = process_contacts_file('contatos_1.vcf')
    contacts5 = process_contacts_file('contatos_1.vcf')

    contacts = contacts1 + contacts2 + contacts3 + contacts4 + contacts5

    whats_mensagem_padrao = urllib.parse.quote("Olá! Aqui é o Eduardo da *Wise Up Online*!")

    context = {
        'contacts': contacts,
        'whats_mensagem_padrao': whats_mensagem_padrao,
    }

    return render(request, 'core/index.html', context)
