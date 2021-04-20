import datetime

from . import authorize

from django.urls import reverse_lazy
from django.contrib.sites.models import Site

calendar_id = '2h4tdljrdegauga7809fvog32o@group.calendar.google.com'


def get_lead_url(lead):
    path =  reverse_lazy('leads:update', args=(str(lead.id),))
    current_site = Site.objects.get_current()
    return str(current_site) + str(path)


def create(activity):

    lead = activity.lead

    service_result = authorize.get_service()

    data = {
        'success': False,
        'result': None,
    }

    if service_result['success']:

        service = service_result['service']

        duration_in_minutes = 35
        
        datetime_format = '%Y-%m-%dT%H:%M:%S'
        
        start_datetime = activity.due_date.strftime(datetime_format) + '-03:00'

        end_datetime = (activity.due_date + datetime.timedelta(minutes=duration_in_minutes)).strftime(datetime_format) + '-03:00'

        lead_url = get_lead_url(lead)

        description = str(lead_url)

        event_dict = {

            'summary': '[WOL] {} '.format(lead),
        
            'description': description,

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

        data = {
            'success': True,
            'calendar_id': calendar_id,
            'event': event,
        }

    return data


def update(activity):

    lead = activity.lead

    service_result = authorize.get_service()

    data = {
        'success': False,
        'result': None,
    }

    if service_result['success']:

        service = service_result['service']

        duration_in_minutes = 35
        
        datetime_format = '%Y-%m-%dT%H:%M:%S'
        
        start_datetime = activity.due_date.strftime(datetime_format) + '-03:00'

        end_datetime = (activity.due_date + datetime.timedelta(minutes=duration_in_minutes)).strftime(datetime_format) + '-03:00'

        lead_url = reverse_lazy('leads:update', args=(str(lead.id),))

        description = str(lead_url)

        event_dict = {

            'summary': '[WOL] {} '.format(lead),
        
            'description': description,

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

        # event = service.events().insert(calendarId=calendar_id, body=event_dict).execute()

        # result = 'Event created: %s' % (event.get('htmlLink'))

        # data = {
        #     'success': False,
        #     'result': result,
        # }

    return data
