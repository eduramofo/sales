from datetime import timedelta
from leads.models import LEAD_STATUS_CHOICES
from django.db import connection


def get_balance_table(account, start_date, end_date):
    rows = get_balance_table_rows(account, start_date, end_date)
    title = 'Balanço dos Leads'
    columns = ['#', 'Variável', 'Valor']
    table_id = 'table-leads-balance'
    table = {
        'title': title,
        'id': table_id,
        'columns': columns,
        'rows': rows,
    }
    return table


def get_balance_table_rows(account, start_date, end_date):
    account_id = str(account.id)
    balance_query = get_balance_query(account_id, start_date, end_date) 
    rows = get_balance_sql_rows(balance_query)
    total = 0
    result = []
    for row in rows:
        title = dict(LEAD_STATUS_CHOICES).get(row[0], row[0])
        value = row[1]
        result.append(
            {'title': title, 'value': value}
        )
        total = total + value
    result.append(
        {'title': 'Total', 'value': total}
    )
    return result


def get_balance_sql_rows(sql_query_string):
    result = None
    if sql_query_string is not None:
        with connection.cursor() as cursor:
            cursor.execute(sql_query_string)
            rows = cursor.fetchall()
            result = rows
    return result


def get_balance_query(account_id, start_date, end_date):
    lt_end_date = end_date + timedelta(days=1)
    query = """
        select status, count(status)
        from (
            select distinct * from leads_lead where id in (
                select lead_id from leads_referrer_leads where referrer_id in (
                    SELECT DISTINCT "leads_referrer"."id"
                    FROM "leads_referrer"
                    WHERE ("leads_referrer"."account_id" = '{}'
                    AND "leads_referrer"."referring_datetime" >= '{}'
                    AND "leads_referrer"."referring_datetime" < '{}')
                )
            )
        ) as leads
    group by status
    """.format(account_id, start_date, lt_end_date)
    return query


def get_leads_generated(account, start_date, end_date):

    lt_end_date = end_date + timedelta(days=1)
    
    sql_query_string = """
        select count(id)
        from (
            select distinct * from leads_lead where id in (
                select lead_id from leads_referrer_leads where referrer_id in (
                    SELECT DISTINCT "leads_referrer"."id"
                    FROM "leads_referrer"
                    WHERE ("leads_referrer"."account_id" = '{}'
                    AND "leads_referrer"."referring_datetime" >= '{}'
                    AND "leads_referrer"."referring_datetime" < '{}')
                )
            )
        ) as leads
    """.format(account.id, start_date, lt_end_date)
    
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
