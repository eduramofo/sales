from urllib.parse import quote
from django.utils.safestring import mark_safe
from django.template import Context, Template
from leads.models import WhatsappTemplate, Referrer
from core.templatetags.core_extras import btn_svg_icons


def whatsapp_api_link_open(lead):
    whatsapp_number = str(lead.waid)
    whatsapp_api_link = 'https://api.whatsapp.com/send'
    link_to_call = whatsapp_api_link + '?phone=' + whatsapp_number
    return link_to_call


def whatsapp_api_all_btns_templates(lead, user_nickname):
    whatsapp_templates = WhatsappTemplate.objects.filter(active=True)
    btns_html = ''
    for template in whatsapp_templates:
        template_name = template.name
        btn_html = make_whatsapp_template_btn_html(lead, user_nickname, template_name)
        btns_html = btns_html + btn_html
    btns_safe = mark_safe(btns_html)
    return btns_safe


def whatsapp_api_btn_template(lead, user_nickname, template_name):
    btn_html = make_whatsapp_template_btn_html(lead, user_nickname, template_name)
    btn_safe = mark_safe(btn_html)
    return btn_safe


def schedule_due_date(lead, user_nickname, template_name, schedule_due_date):
    waid = lead.waid
    template_object = get_object_or_none(WhatsappTemplate, name=template_name)
    link = '#'
    if waid and template_object:
        text = template_object.content
        template = Template(text)
        context = get_context(lead, user_nickname)
        print(schedule_due_date)
        context['schedule_due_date'] = schedule_due_date
        context = Context(context)
        raw_text_context = template.render(context)
        text = quote(raw_text_context)
        whatsapp_api_endpoint = 'https://api.whatsapp.com'
        whatsapp_api_link = '{}/send?phone={}'.format(whatsapp_api_endpoint, waid)
        link = '{}&text={}'.format(whatsapp_api_link, text)
        link = mark_safe(link)
    return link


def make_whatsapp_template_btn_html(lead, user_nickname, template_name):
    waid = lead.waid
    template_object = get_object_or_none(WhatsappTemplate, name=template_name)
    btn_html = ''
    if waid and template_object:
        btn_text = template_object.title
        btn_href = make_whastapp_api_link(waid, template_object, lead, user_nickname)
        btn_html = make_btn(btn_text, btn_href)
    return btn_html


def make_whastapp_api_link(waid, template_object, lead, user_nickname):
    content = template_object.content
    text = make_text_quote(content, lead, user_nickname)
    whatsapp_api_endpoint = 'https://api.whatsapp.com'
    whatsapp_api_link = '{}/send?phone={}'.format(whatsapp_api_endpoint, waid)
    whastapp_api_link = '{}&text={}'.format(whatsapp_api_link, text)
    return whastapp_api_link


def make_text_quote(raw_text, lead, user_nickname):
    text = ''
    if raw_text:
        raw_text_context = adjust_context(raw_text, lead, user_nickname)
        text = quote(raw_text_context)
    return text


def adjust_context(text, lead, user_nickname):
    template = Template(text)
    context_ = get_context(lead, user_nickname)
    context__ = Context(context_)
    return template.render(context__)


def get_context(lead, user_nickname):
    
    lead_first_name = str(lead.name).partition(' ')[0]
    
    if lead_first_name:
        lead_first_name = lead_first_name.capitalize()
    else:
        lead_first_name = ''

    # referrer
    referrer_first_name = ''
    referrer_full_name = ''
    referrers = Referrer.objects.filter(leads=lead)
    if len(referrers) > 0:
        referrer = referrers.first()
        referrer_lead = referrers.first().lead
        if referrer_lead:
            referrer_name = str(referrer_lead)
        else:
            referrer_name = referrer.name

        referrer_first_name = referrer_name.partition(' ')[0].capitalize().strip()
        referrer_last_name = referrer_name.partition(' ')[2].capitalize().strip()
        if referrer_last_name:
            referrer_full_name = '{} {}'.format(referrer_first_name, referrer_last_name).strip()
        else:
            referrer_full_name = referrer_first_name

    context = {
        'user_nickname': user_nickname,
        'lead_first_name': lead_first_name,
        'referrer_first_name': referrer_first_name,
        'referrer_full_name': referrer_full_name,
    }

    return context


def get_object_or_none(classmodel, **kwargs):
    try: 
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def make_btn(btn_text, btn_href):
    btn_icon_and_text = btn_svg_icons('custom', 'whatsapp-fill', '25px', 'left', btn_text)
    btn_id = 'whatsapp-btn-templates-'
    btn_class = 'btn btn-lg btn-block btn-secondary text-left'
    btn_html = '<a role="button" id="{}" class="{}" href="{}">{}</a>'.format(btn_id, btn_class, btn_href, btn_icon_and_text)
    return btn_html
