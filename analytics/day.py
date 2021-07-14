from leads import models as leads_models


def get_data_clean(activities):

    data = {}

    # activities
    activities_count = activities.count()

    # leads
    leads_pks = activities.values_list('lead', flat=True).distinct()
    leads = leads_models.Lead.objects.filter(pk__in=leads_pks)
    leads_count = leads.count()
    leads_win = leads.filter(status='ganho').count()

    contact_attempts = ['tentando_contato', 'tentando_contato_2', 'geladeira', 'ghosting', 'ghosting_2', 'ultimatum', 'agendamento_direct']
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

    #### off
    leads_off = leads.filter(status='off').count()

    #### conversations
    leads_conversations = leads_lost_sem_interesse + leads_lost_di + leads_lost_entrevista + leads_win + leads_schedules + leads_off

    #### speechs
    leads_speechs = leads_lost_entrevista + leads_win + leads_off

    attendance_rate = 'N/A'
    if activities_count > 0:
        attendance_rate = round(leads_conversations / activities_count * 100, 1)
        attendance_rate = str(attendance_rate).replace('.', ',') + '%'

    speech_rate = 'N/A'
    if leads_conversations > 0:
        speech_rate = round(leads_speechs / leads_conversations * 100, 1)
        speech_rate = str(speech_rate).replace('.', ',') + '%'

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
            {'title': 'Entrevistas: Totais', 'value': leads_speechs},
            {'title': 'Entrevistas: Perdidas', 'value': leads_lost_entrevista},
            {'title': 'Entrevistas: Off', 'value': leads_off},
            {'title': 'Entrevistas: Matrículas', 'value': leads_win},
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
            {'title': 'Entrevistas: Totais', 'value': leads_speechs},
            {'title': 'Entrevistas: Perdidas', 'value': leads_lost_entrevista},
            {'title': 'Entrevistas: Off', 'value': leads_off},
            {'title': 'Entrevistas: Matrículas', 'value': leads_win},
        ],

    }

    data['summary'] = {

        'id': 'table-summary',

        'title': 'Sumário do Dia',

        'columns': ['#', 'Variável', 'Valor'],

        'rows': [
            {'title': 'Atividades', 'value': activities_count},
            {'title': 'Conversas', 'value': leads_conversations},
            {'title': 'Entrevistas', 'value': leads_speechs},
            {'title': 'Matrículas', 'value': leads_win},
            {'title': 'Taxa de Conversas', 'value': attendance_rate},
            {'title': 'Taxa de Entrevistas', 'value': speech_rate},
            {'title': 'Referidos', 'value': 'N/A'},
        ],

    }

    return data
