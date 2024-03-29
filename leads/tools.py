from django.db.models import Q

from leads.models import Lead


def get_open_leads():
    leads_exclude_filter = Q(status='sem_interesse') | Q(status='sem_condicoes_financeiras') | Q(status='contato_invalido') | Q(status='ignorando') | Q(status='agendamento') | Q(status='acompanhamento') | Q(status='perdido') | Q(status='ganho')
    leads_open_filter = Lead.objects.exclude(leads_exclude_filter).order_by('-created_at')
    return leads_open_filter


def get_open_run_now_leads(account):
    open_leads = get_open_leads()
    return open_leads.filter(account=account, run_now=True)


def get_referrers_next_lead(lead):
    return '1'
