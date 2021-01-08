from urllib.parse import quote
from django.shortcuts import get_object_or_404
from leads.models import WhatsappTemplate


def whatsapp_template_api_link(lead, template_name):
    waid = lead.waid
    if lead.waid:
        text = make_tlp(template_name, {})
        whastapp_api_link = make_whastapp_api_link(waid, text)
        return whastapp_api_link
    else:
        return '#'


def whatsapp_template_api_link_all(lead):
    return '#'


def make_whastapp_api_link(waid, text):
    whatsapp_api_link = 'https://api.whatsapp.com/send?phone={}'.format(waid)
    whastapp_api_link = '{}&text={}'.format(whatsapp_api_link, text)
    return whastapp_api_link


def make_tlp(template_name, context):
    template = get_object_or_404(WhatsappTemplate, name=template_name)
    raw_text = template.content
    text = quote(raw_text)
    return text
