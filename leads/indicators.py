from django.db import connection
from collections import namedtuple


# https://docs.djangoproject.com/en/3.1/topics/db/sql/#executing-custom-sql-directly
def indicators_data():
    results = None
    sql_query = 'select distinct indicated_by from leads_lead'
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        results = namedtuplefetchall(cursor)
    return results


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    description = cursor.description
    nt_result = namedtuple(
        'result',
        [col[0] for col in description],
    )
    return [ nt_result(*row) for row in cursor.fetchall() ]
