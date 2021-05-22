from leads import models as leads_models


def get_data_clean(activities):
    
    data = {}
    
    # activities
    activities_count = activities.count()

    # leads
    leads_pks = leads_processed = activities.values_list('lead', flat=True).distinct()
    leads = leads_models.Lead.objects.filter(pk__in=leads_pks)
    leads_count = leads.count()
    leads_win = leads.filter(status='ganho').count()

    contact_attempts = ['tentando_contato', 'tentando_contato_2', 'geladeira', 'ghosting', 'ghosting_2', 'ultimatum']
    leads_contact_attempts = leads.filter(status__in=contact_attempts).count()

    #### LOST
    ##### conversations
    leads_lost = leads.filter(status='perdido').count()
    leads_lost_sem_interesse = leads.filter(status='perdido', status_lost_justification='sem_interesse').count()
    leads_lost_di = leads.filter(status='perdido', status_lost_justification='di').count()
    leads_lost_entrevista = leads.filter(status='perdido', status_lost_justification='entrevista_perdida').count()
    ##### direct
    leads_lost_direct = leads.filter(status='perdido', status_lost_justification='lost_direct').count()

    #### schedules
    leads_schedules = leads.filter(status='agendamento',).count()

    #### conversations
    leads_conversations = leads_lost_sem_interesse + leads_lost_di + leads_lost_entrevista + leads_win + leads_schedules

    #### speechs
    leads_speechs = leads_lost_entrevista + leads_win

    attendance_rate = 'N/A'
    if activities_count > 0:
        attendance_rate = round(leads_conversations / activities_count * 100, 1)
        attendance_rate = str(attendance_rate).replace('.', ',') + '%'
    else:
        pass

    data['leads'] = {

        'id': 'table-leads',

        'title': 'Leads',

        'columns': ['#', 'Variável', 'Valor'],

        'rows': [
            {'title': 'Total', 'value': leads_count},
            {'title': 'Tentativas', 'value': leads_contact_attempts},
            {'title': 'Perdidos Direto', 'value': leads_lost_direct},
            {'title': 'Conversas', 'value': leads_conversations},
            {'title': 'Sem Interesse', 'value': leads_lost_sem_interesse},
            {'title': 'Agendamentos', 'value': leads_schedules},
            {'title': 'DI', 'value': leads_lost_di},
            {'title': 'Entrevistas Totais', 'value': leads_speechs},
            {'title': 'Entrevistas Perdidas', 'value': leads_lost_entrevista},
            {'title': 'Entrevistas Matrículas', 'value': leads_win},
        ],

    }

    data['conversations'] = {

        'id': 'table-conversations',

        'title': 'Conversas',

        'columns': [
            '#', 'Variável', 'Valor'
        ],

        'rows': [
            {'title': 'Conversas', 'value': leads_conversations},
            {'title': 'Sem Interesse', 'value': leads_lost_sem_interesse},
            {'title': 'Agendamentos', 'value': leads_schedules},
            {'title': 'DI', 'value': leads_lost_di},
            {'title': 'Entrevistas Totais', 'value': leads_speechs},
            {'title': 'Entrevistas Perdidas', 'value': leads_lost_entrevista},
            {'title': 'Entrevistas Matrículas', 'value': leads_win},
        ],

    }

    data['summary'] = {

        'id': 'table-summary',

        'title': 'Sumário do Dia',

        'columns': ['#', 'Variável', 'Valor'],

        'rows': [
            {'title': 'Atividades', 'value': activities_count},
            {'title': 'Tentativas sem Sucesso', 'value': leads_contact_attempts},
            {'title': 'Conversas', 'value': leads_conversations},
            {'title': 'Entrevistas', 'value': leads_speechs},
            {'title': 'Matrículas', 'value': leads_win},
            {'title': 'Referidos', 'value': 'N/A'},
            {'title': 'Taxa de Atendimento', 'value': attendance_rate},
        ],

    }

    return data
