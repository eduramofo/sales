import urllib.parse
import json

from django.db.models import Q
from django import template
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.template.defaultfilters import date

from leads.models import Lead, Referrer
from leads.whatsapp import api as whatsapp_api
from activities.models import Activity


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
def whatsapp_api_link_open(lead):
    return whatsapp_api.whatsapp_api_link_open(lead)


@register.simple_tag
def whatsapp_api_btn_template(lead, user_nickname, template_name):
    return whatsapp_api.whatsapp_api_btn_template(lead, user_nickname, template_name)


@register.simple_tag
def whatsapp_api_all_btns_templates(lead, user_nickname):
    return whatsapp_api.whatsapp_api_all_btns_templates(lead, user_nickname)


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
def get_referrers_from_lead_first_referring_datetime(lead):
    referrer_obj = Referrer.objects.filter(leads=lead).first()
    if referrer_obj:
        return referrer_obj.referring_datetime
    return None


@register.filter
def get_referrers_from_lead_first_name(lead):
    referrer_obj = Referrer.objects.filter(leads=lead).first()
    if referrer_obj:
        return referrer_obj.name
    return None


@register.filter
def show_next_activities(lead):
    result = 'Não Existe'
    activity_qs = Activity.objects.filter(lead=lead, done=False).order_by('due_date')
    if len(activity_qs) > 0:
        due_date = activity_qs.first().due_date
        if due_date:
            result = date(due_date, 'd/M/y à\s H:i')
    return result


@register.filter
def get_opened_leads(referrer):
    leads_filter_query = Q(status='novo') | Q(status='tentando_contato') | Q(status='processando') | Q(status='agendamento')
    leads = referrer.leads.filter(leads_filter_query)
    return leads


@register.filter
def get_closed_leads(referrer):
    leads_filter_query = Q(status='perdido') | Q(status='ganho')
    leads = referrer.leads.filter(leads_filter_query)
    return leads


@register.filter
def get_news_leads(referrer):
    leads_filter_query = Q(status='novo')
    leads = referrer.leads.filter(leads_filter_query)
    return leads


@register.filter
def get_tentanto_leads(referrer):
    leads_filter_query = Q(status='tentando_contato')
    leads = referrer.leads.filter(leads_filter_query)
    return leads


@register.filter
def get_ganho_leads(referrer):
    leads_filter_query = Q(status='ganho')
    leads = referrer.leads.filter(leads_filter_query)
    return leads


@register.filter
def get_perdido_leads(referrer):
    leads_filter_query = Q(status='perdido')
    leads = referrer.leads.filter(leads_filter_query)
    return leads


@register.filter
def get_agendamento_leads(referrer):
    leads_filter_query = Q(status='agendamento')
    leads = referrer.leads.filter(leads_filter_query)
    return leads


@register.filter
def get_follow_up_leads(referrer):
    leads_filter_query = Q(status='acompanhamento')
    leads = referrer.leads.filter(leads_filter_query)
    return leads
