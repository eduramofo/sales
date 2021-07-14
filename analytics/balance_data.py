from leads import models


def get_data():

    data = {}

    all_leads = models.Lead.objects.all()

    leads_statuses = all_leads.values('status').distinct()

    rows = [] 
    for status_row in leads_statuses:
        current_status = status_row['status']
        current_status_count = all_leads.filter(status=current_status).count
        rows.append(
            {'title': current_status, 'value': current_status_count}
        )
    
    rows.append(
        {'title': 'Total', 'value': all_leads.count}
    ) 

    data['balance'] = {

        'id': 'table-leads',

        'title': 'Balanço dos Leads',

        'columns': ['#', 'Variável', 'Valor'],

        'rows': rows,

    }

    return data
