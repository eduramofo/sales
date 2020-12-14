import urllib.parse
import json

from django.db.models import Q
from django import template
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from leads.models import Lead, Referrer

register = template.Library()


@register.simple_tag
def link_to_call_lead(lead_object):

    # BR CHECK
    tel = str(lead_object.tel)
    tel_temp = tel.replace(" ", "").replace("-", "")
    br_ddi = '+55'
    tel_ddi_check_br = tel[:3]
    if tel_ddi_check_br == br_ddi:
        ddd = tel_temp[3:5]
        tel_temp = tel_temp[5:]
        tel_size = len(tel_temp)
        if tel_size == 8:
            tel =  br_ddi + " " + ddd + " " + str(9) + tel_temp
    # BR CHECK


    link_to_call = 'tel:' + tel

    return link_to_call


@register.simple_tag
def link_whats_open(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send'

    link_to_call = whatsapp_api_link + '?phone=' + whatsapp_number

    return link_to_call


@register.simple_tag
def link_whats_oi(lead_object):
    
    whatsapp_number = str(lead_object.waid)
    
    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number
    
    text = 'Ol%C3%A1%20Aqui%20%C3%A9%20o%20Eduardo%20da%20*Wise%20Up%20Online*!'
    
    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def link_wise_up_link(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number

    text = 'https%3A%2F%2Fwup.onl%2F0031R00002Dv1itQAB'

    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def link_wise_up_boleto_link(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number

    text = 'https%3A%2F%2Fwup.onl%2F0031R00002Dv1itQAB/boleto'

    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def link_whats_tentei_te_ligar(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number
    
    lead_name = str(lead_object.name).partition(' ')[0]

    indicated_by_first_name = str(lead_object.indicated_by).partition(' ')[0]

    raw_text = 'Olá ' + lead_name + ', tudo bem? Aqui e o Eduardo. Estou te contatando através do(a) ' + indicated_by_first_name + '. Você pode falar agora?'

    text = urllib.parse.quote(raw_text)
    
    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def link_modelo_referido_conheci(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number

    raw_text = "Conheci um projeto para aprender Inglês da *Wise Up* e te indiquei. Acho que você também vai gostar! 🚀🇺🇸. O representante *Eduardo* da *Wise Up* vai te ligar para te apresentar, Ok? O número dele é esse: *(31) 99569-1349*."

    text = urllib.parse.quote(raw_text)

    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def link_modelo_referido_entrei(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number

    raw_text = "Entrei em um projeto para aprender Inglês da *Wise Up* e te indiquei. Acho que você também vai gostar! 🚀🇺🇸. O representante *Eduardo* da *Wise Up* vai te ligar para te apresentar, Ok? O número dele é esse: *(31) 99569-1349*."

    text = urllib.parse.quote(raw_text)

    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def run_now_table_data_html(lead_id, lead_run_now):

    url = ''
    data = {}
    td_html = "<td class='run-now-td' data-run-now-data='{}' data-run-now-url='{}'><strong class='{}'>{}</strong></td>"
    
    if lead_run_now == True:
        url = reverse_lazy('leads:update-run-now', args=(str(lead_id), 'true',))
        data = {'run_now': False,}
        data = json.dumps(data)
        td_html = td_html.format(data, url, 'text-success', 'Sim')
    
    elif lead_run_now == False:
        url = reverse_lazy('leads:update-run-now', args=(str(lead_id), 'false',))
        data = {'run_now': True,}
        data = json.dumps(data)
        td_html = td_html.format(data, url, 'text-danger','Não')
    
    else:
        data = json.dumps(data)
        td_html = td_html.format(data, url, 'text-danger','Não')

    return mark_safe(td_html)


@register.filter
def get_referrers_from_lead(lead):
    return Referrer.objects.filter(leads=lead)


@register.filter
def get_opened_leads(referrer):
    leads_filter_query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando') | Q(status='agendamento')
    leads = referrer.leads.filter(leads_filter_query)
    return leads
