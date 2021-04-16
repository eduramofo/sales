# thirds
import json

# google api
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials


# django
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# app
from integrations.models import GoogleApi


def get_credentials():
    identifier = 'GOOGLE_CALENDAR'
    google_calendar_api = get_object_or_404(
        GoogleApi,
        identifier=identifier
    )
    credentials_dict = json.loads(google_calendar_api.o_auth_2_token_json)
    credentials = Credentials(
        credentials_dict["token"],
        refresh_token = credentials_dict["refresh_token"],
        token_uri = credentials_dict["token_uri"],
        client_id = credentials_dict["client_id"],
        client_secret = credentials_dict["client_secret"],
        scopes = credentials_dict["scopes"]
    )
    return credentials


def set_credentials(credentials):
    identifier = 'GOOGLE_CALENDAR'
    google_calendar_api = get_object_or_404(
        GoogleApi,
        identifier=identifier
    )
    google_calendar_api.o_auth_2_token_json = credentials
    google_calendar_api.save()
    return google_calendar_api


def get_client_secret():
    identifier = 'GOOGLE_CALENDAR'
    google_calendar_api = get_object_or_404(
        GoogleApi,
        identifier=identifier
    )
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


def credentials_to_json_string(credentials):
    credentials_dict = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes,
    }
    credentials_json_string = json.dumps(credentials_dict)
    return credentials_json_string


def get_servide():
    credentials = get_credentials()
    service = build('calendar', 'v3', credentials=credentials)
    return service


def authorize(request):
    SCOPES = [
        'https://www.googleapis.com/auth/calendar',
    ]
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
    credentials = flow.credentials
    credentials_json_string = credentials_to_json_string(credentials)
    set_credentials(credentials_json_string)
    success_url = reverse_lazy('integrations:google_calendar:oauth2success', args=())
    return success_url


def success():
    service = get_servide()
    calendar = service.calendars().get(calendarId='primary').execute()
    data = {'success': True, 'result': calendar['summary'],}
    return data
