from datetime import timedelta
from analytics.balance import get_leads_generated
from activities.models import Activity
from conversation.models import Conversation
from django.db import connection


def get_production_table(account, start_date_obj, end_date_obj):
    activities = get_activities(account, start_date_obj, end_date_obj)
    conversations = get_conversations(account, start_date_obj, end_date_obj)
    speechs = get_speechs(account, start_date_obj, end_date_obj)
    win = get_speechs_win(account, start_date_obj, end_date_obj)
    leads_generated = get_leads_generated(account, start_date_obj, end_date_obj)
    leads_consumed = get_leads_consumed(account, start_date_obj, end_date_obj)
    result = get_summary_table(activities, conversations, speechs, win, leads_generated, leads_consumed)
    return result


def get_activities(account, start_date_obj, end_date_obj):
    lt_end_date = end_date_obj + timedelta(days=1)
    activities = Activity.objects.filter(
        account=account,
        created_at__gte=start_date_obj,
        created_at__lte=lt_end_date,
    ).exclude(subject='Inválido')
    return activities


def get_conversations(account, start_date_obj, end_date_obj):
    lt_end_date = end_date_obj + timedelta(days=1)
    conversation_qs = Conversation.objects.filter(
        account=account,
        created_at__gte=start_date_obj,
        created_at__lte=lt_end_date,
    )
    return conversation_qs.values_list('lead', flat=True).distinct().count()


def get_speechs(account, start_date_obj, end_date_obj):
    lt_end_date = end_date_obj + timedelta(days=1)
    conversation_qs = Conversation.objects.filter(
        account=account,
        created_at__gte=start_date_obj,
        created_at__lte=lt_end_date,
        type__in=['lost', 'win', 'off'],
    )
    return conversation_qs.values_list('lead', flat=True).distinct().count()


def get_speechs_win(account, start_date_obj, end_date_obj):
    lt_end_date = end_date_obj + timedelta(days=1)
    conversation_qs = Conversation.objects.filter(
        account=account,
        created_at__gte=start_date_obj,
        created_at__lte=lt_end_date,
        type__in=['lost', 'win', 'off'],
    )
    return conversation_qs.values_list('lead', flat=True).distinct().count()


def get_leads_consumed(account, start_date_obj, end_date_obj):
    account_id = account.id
    lt_end_date = end_date_obj + timedelta(days=1)
    sql_query_string = """
    select count(id) from 
    (select distinct * from leads_lead
    where 
    id in (
        select lead_id from activities_activity
        where "activities_activity"."account_id" = '{}'
        and "activities_activity"."due_date" >= '{}'
        and "activities_activity"."due_date" < '{}'
    ) and status not in ('novo', 'tentando_contato', 'tentando_contato')
    ) as leads
    """.format(account_id, start_date_obj, lt_end_date)
    result = None
    if sql_query_string is not None:
        with connection.cursor() as cursor:
            cursor.execute(sql_query_string)
            result = cursor.fetchone()
    if result is not None:
        try:
            result = result[0]
        except:
            result = 'ERROR'
    return result


def get_summary_table(activities, conversations, speechs, win, leads_generated, leads_consumed):

    activities = activities.count()

    attendance_rate = 'N/A'
    if activities > 0:
        attendance_rate = round(conversations / activities * 100, 1)
        attendance_rate = str(attendance_rate).replace('.', ',') + '%'

    speech_rate = 'N/A'
    if conversations > 0:
        speech_rate = round(speechs / conversations * 100, 1)
        speech_rate = str(speech_rate).replace('.', ',') + '%'

    win_rate = 'N/A'
    if speechs > 0:
        win_rate = round(win / speechs * 100, 1)
        win_rate = str(win_rate).replace('.', ',') + '%'

    leads_balance = 'N/A'
    leads_rate = 'N/A'
    if leads_generated != 'ERROR' and leads_generated is not None:
        if leads_consumed != 'ERROR' and leads_consumed is not None:
            leads_balance = leads_generated - leads_consumed
            if leads_consumed > 0:
                leads_rate = round(leads_generated / leads_consumed, 1)
                leads_rate = str(leads_rate).replace('.', ',')

    table = {
        'title': 'Sumário do Dia',
        'id': 'table-summary',
        'columns': ['#', 'Variável', 'Valor'],
        'rows': [
            {'title': 'Atividades', 'value': activities},
            {'title': 'Conversas', 'value': conversations},
            {'title': 'Entrevistas', 'value': speechs},
            {'title': 'Matrículas', 'value': win},
            {'title': 'Leads Gerados', 'value': leads_generated},
            {'title': 'Leads Consumidos', 'value': leads_consumed},
            {'title': 'Saldo de Leads', 'value': leads_balance},
            {'title': 'Taxa de Leads Ref.: > 1', 'value': leads_rate},
            {'title': 'Taxa de Conversas', 'value': attendance_rate},
            {'title': 'Taxa de Entrevistas', 'value': speech_rate},
            {'title': 'Taxa de Matrículas', 'value': win_rate},
        ],
    }

    return table
