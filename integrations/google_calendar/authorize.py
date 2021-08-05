# thirds
import json

# google api
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# django
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# app
from integrations.models import GoogleApi


SCOPES = [
    'https://www.googleapis.com/auth/calendar'
]

def get_google_calendar_id():
    return get_google_calendar_api_obj().calendar_id


def get_google_calendar_api_obj():
    identifier = 'GOOGLE_CALENDAR'
    google_calendar_api = get_object_or_404(
        GoogleApi,
        identifier=identifier
    )
    return google_calendar_api


def get_credentials():
    google_calendar_api = get_google_calendar_api_obj()    
    credentials = Credentials(
        google_calendar_api.o_auth_2_credentials_token,
        refresh_token=google_calendar_api.o_auth_2_credentials_refresh_token,
        token_uri=google_calendar_api.o_auth_2_credentials_token_uri,
        client_id=google_calendar_api.o_auth_2_credentials_client_id,
        client_secret=google_calendar_api.o_auth_2_credentials_client_secret,
        scopes = SCOPES,
    )
    return credentials


def set_credentials(credentials):
    token = credentials.token
    refresh_token = credentials.refresh_token
    token_uri = credentials.token_uri
    client_id = credentials.client_id
    client_secret = credentials.client_secret
    google_calendar_api = get_google_calendar_api_obj()
    if refresh_token:
        google_calendar_api.o_auth_2_credentials_refresh_token = refresh_token
    google_calendar_api.o_auth_2_credentials_token = token
    google_calendar_api.o_auth_2_credentials_token_uri = token_uri
    google_calendar_api.o_auth_2_credentials_client_id = client_id
    google_calendar_api.o_auth_2_credentials_client_secret = client_secret
    google_calendar_api.o_auth_2_credentials_scopes = None
    google_calendar_api.save()


def get_client_secret():
    google_calendar_api = get_google_calendar_api_obj()
    return google_calendar_api.o_auth_2_client_secret_json


def get_callback_url(request):
    base = '{}://{}'.format(request.scheme, request.META['HTTP_HOST'])
    path = str(reverse_lazy('integrations:google_calendar:oauth2callback', args=()))
    full_url = '{}{}'.format(base, path)    
    return full_url


def get_client_config():
    client_secret = get_client_secret()
    client_config = json.loads(client_secret)
    return client_config


def get_service():
    credentials = get_credentials()
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
        set_credentials(credentials)
    result = {
        'success': False,
        'service': None,
    }
    if credentials and credentials.valid:
        service = build(
            'calendar',
            'v3',
            credentials=credentials
        )
        result = {
            'success': True,
            'service': service,
        }
    else:
        print('Need login again!')
    return result


def authorize(request):
    flow = InstalledAppFlow.from_client_config(get_client_config(), scopes=SCOPES,)
    flow.redirect_uri = get_callback_url(request)
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true'
    )
    return authorization_url


def callback(request):
    state = request.GET.get('state')
    code = request.GET.get('code')
    scopes = request.GET.get('scope')
    flow = InstalledAppFlow.from_client_config(get_client_config(), scopes=scopes, state=state)
    flow.redirect_uri = get_callback_url(request)
    flow.fetch_token(code=code)
    set_credentials(flow.credentials)
    success_url = reverse_lazy('integrations:google_calendar:oauth2success', args=())
    return success_url


def success():
    service_result = get_service()
    data = {'success': False,}
    if service_result['success']:
        service = service_result['service']
        calendar = service.calendars().get(calendarId='primary').execute()
        data = {
            'success': True,
            'result': calendar['summary'],
        }
    return data
