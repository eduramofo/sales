from leads import models as leads_models


def data(activities, conversations, speechs, win):
    
    data = {}
    activities = activities.count()

    attendance_rate = 'DIV/0!'
    if activities > 0:
        attendance_rate = round(conversations / activities * 100, 1)
        attendance_rate = str(attendance_rate).replace('.', ',') + '%'

    speech_rate = 'DIV/0!'
    if conversations > 0:
        speech_rate = round(speechs / conversations * 100, 1)
        speech_rate = str(speech_rate).replace('.', ',') + '%'

    win_rate = 'DIV/0!'
    if speechs > 0:
        win_rate = round(win / speechs * 100, 1)
        win_rate = str(win_rate).replace('.', ',') + '%'

    referrals = 'N/A'

    data['summary'] = {
        'id': 'table-summary',
        'title': 'Sumário do Dia',
        'columns': ['#', 'Variável', 'Valor'],
        'rows': [
            {'title': 'Atividades', 'value': activities},
            {'title': 'Conversas', 'value': conversations},
            {'title': 'Entrevistas', 'value': speechs},
            {'title': 'Matrículas', 'value': win},
            {'title': 'Referidos', 'value': referrals},
            {'title': 'Taxa de Conversas', 'value': attendance_rate},
            {'title': 'Taxa de Entrevistas', 'value': speech_rate},
            {'title': 'Taxa de Matrículas', 'value': win_rate},
        ],
    }

    return data
