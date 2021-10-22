import datetime

from . import authorize

from django.urls import reverse_lazy
from django.contrib.sites.models import Site
from integrations.google_calendar.authorize import get_google_calendar_id


def get_lead_url(lead):
    if lead:
        path =  reverse_lazy('leads:update', args=(str(lead.id),))
        current_site = Site.objects.get_current()
        return str(current_site) + str(path)
    else:
        return ''


def create(event):
    lead = event.lead
    service_result = authorize.get_service()
    calendar_id = get_google_calendar_id()
    data = {
        'success': False,
        'result': None,
    }
    if service_result['success']:
        service = service_result['service']
        datetime_format = '%Y-%m-%dT%H:%M:%S'
        start_datetime = event.start_datetime.strftime(datetime_format) + '-03:00'
        end_datetime = event.end_datetime.strftime(datetime_format) + '-03:00'
        lead_url = get_lead_url(lead)
        description = str(lead_url)
        event_dict = {

            'summary': event.summary,
        
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


def update(event_obj):
    data = {
        'success': False,
        'result': None,
    }
    calendar_id = event_obj.google_calendar_calendar_id
    event_id = event_obj.google_calendar_event_id
    if calendar_id is not None and event_id is not None:
        service_result = authorize.get_service()
        if service_result['success']:
            service = service_result['service']
            event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
            datetime_format = '%Y-%m-%dT%H:%M:%S'
            start_datetime = event.start_datetime.strftime(datetime_format) + '-03:00'
            end_datetime = event.end_datetime.strftime(datetime_format) + '-03:00'
            event['start']['dateTime'] = start_datetime
            event['end']['dateTime'] = end_datetime
            updated_event = service.events().update(calendarId=calendar_id, eventId=event['id'], body=event).execute()
            data = {
                'success': True,
                'calendar_id': calendar_id,
                'event': updated_event,
            }
    return data


def get_event_data_from_event():
    pass
