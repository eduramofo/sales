from django import template
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from leads.models import Lead
import urllib.parse

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
def link_whats_tentei_te_ligar(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number
    
    lead_name = str(lead_object.name).partition(' ')[0]

    indicated_by_first_name = str(lead_object.indicated_by).partition(' ')[0]

    raw_text = 'Olá ' + lead_name + ', tudo bem? Aqui e o Eduardo e estou te contatando através da sua amiga ' + indicated_by_first_name + '. Você pode falar?'

    text = urllib.parse.quote(raw_text)
    
    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def link_modelo_referido_conheci(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number

    text = 'Conheci%20um%20projeto%20para%20aprender%20ingl%C3%AAs%20da%20*Wise%20Up*%20e%20te%20indiquei.%20Acho%20que%20voc%C3%AA%20tamb%C3%A9m%20vai%20gostar!%20%F0%9F%9A%80%F0%9F%87%BA%F0%9F%87%B8%20%20O%20representante%20*Eduardo*%20da%20*Wise%20Up*%20vai%20te%20ligar%20pra%20apresentar%2C%20ok%3F%20O%20n%C3%BAmero%20dele%20%C3%A9%20esse%3A%20*(31)%2099569-1349*.%20%20Caso%20voc%C3%AA%20*N%C3%83O%20TENHA%20INTERESSE*%20em%20aprender%20Ingl%C3%AAs%20%F0%9F%91%89%20CLICA%20no%20link%20abaixo%20e%20avisa%20ele%20(dessa%20forma%20ele%20nem%20te%20liga).%20%F0%9F%91%87%20%E2%9D%8C%20http%3A%2F%2Fbit.ly%2Fwol-nao-tenho-interesse%20%20Caso%20voc%C3%AA%20*TENHA%20INTERESSE*%20em%20aprender%20Ingl%C3%AAs%20%F0%9F%91%89%20CLICA%20no%20link%20abaixo%2C%20pois%20assim%20ele%20te%20prioriza%20nos%20atendimentos.%20%F0%9F%91%87%20%E2%9C%85%20http%3A%2F%2Fbit.ly%2Fwol-tenho-interesse'

    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def link_modelo_referido_entrei(lead_object):

    whatsapp_number = str(lead_object.waid)

    whatsapp_api_link = 'https://api.whatsapp.com/send?phone=' + whatsapp_number

    text = 'Entrei%20em%20um%20projeto%20para%20aprender%20ingl%C3%AAs%20da%20*Wise%20Up*%20e%20te%20indiquei.%20Acho%20que%20voc%C3%AA%20tamb%C3%A9m%20vai%20gostar!%20%F0%9F%9A%80%F0%9F%87%BA%F0%9F%87%B8%20%20O%20representante%20*Eduardo*%20da%20*Wise%20Up*%20vai%20te%20ligar%20pra%20apresentar%2C%20ok%3F%20O%20n%C3%BAmero%20dele%20%C3%A9%20esse%3A%20*(31)%2099569-1349*.%20%20Caso%20voc%C3%AA%20*N%C3%83O%20TENHA%20INTERESSE*%20em%20aprender%20Ingl%C3%AAs%20%F0%9F%91%89%20CLICA%20no%20link%20abaixo%20e%20avisa%20ele%20(dessa%20forma%20ele%20nem%20te%20liga).%20%F0%9F%91%87%20%E2%9D%8C%20http%3A%2F%2Fbit.ly%2Fwol-nao-tenho-interesse%20%20Caso%20voc%C3%AA%20*TENHA%20INTERESSE*%20em%20aprender%20Ingl%C3%AAs%20%F0%9F%91%89%20CLICA%20no%20link%20abaixo%2C%20pois%20assim%20ele%20te%20prioriza%20nos%20atendimentos.%20%F0%9F%91%87%20%E2%9C%85%20http%3A%2F%2Fbit.ly%2Fwol-tenho-interesse'

    link_to_call = whatsapp_api_link + '&text=' + text

    return link_to_call


@register.simple_tag
def run_now_table_data_html(lead_id, lead_run_now):

    url = ''
    
    td_html = "<td class='run-now-td' data-run-now-url='{}'><strong class='{}'>{}</strong></td>"
    
    if lead_run_now == True:
        url = reverse_lazy('leads:update-run-now', args=(str(lead_id), 'true',))
        td_html = td_html.format(url, 'text-success', 'Sim')
    
    elif lead_run_now == False:
        url = reverse_lazy('leads:update-run-now', args=(str(lead_id), 'false',))
        td_html = td_html.format(url, 'text-danger','Não')

    else:
        td_html = td_html.format(url, 'N/A')

    return mark_safe(td_html)
