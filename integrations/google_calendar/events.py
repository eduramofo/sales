import datetime

from . import authorize

calendar_id = '2h4tdljrdegauga7809fvog32o@group.calendar.google.com'


def create(activity):

    lead = activity.lead

    service = authorize.get_servide()

    duration_in_minutes = 35
    
    datetime_format = '%Y-%m-%dT%H:%M:%S'
    
    start_datetime = activity.due_date.strftime(datetime_format) + '-03:00'
    
    end_datetime = (activity.due_date + datetime.timedelta(minutes=duration_in_minutes)).strftime(datetime_format) + '-03:00'

    event_dict = {

        'summary': '{} [ Wise Up Online ]'.format(lead),
      
        'description': 'https://azaper.com/leads/a8551026-52e3-4c8c-995a-e385f474e071/update/',
        
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'America/Sao_Paulo',
        },

        'end': {
            'dateTime': end_datetime,
            'timeZone': 'America/Sao_Paulo',
        },

        'reminders': {

            'useDefault': False,

            'overrides': [
                {'method': 'popup', 'minutes': 5},
            ],

        },

    }

    event = service.events().insert(calendarId=calendar_id, body=event_dict).execute()

    result = 'Event created: %s' % (event.get('htmlLink'))

    data = {
        'success': True,
        'result': result,
    }

    return data
