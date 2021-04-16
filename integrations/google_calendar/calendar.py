# from __future__ import print_function
# sys
import os.path

# external
import datetime
import json

# google api
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# django
from django.conf import settings
from django.shortcuts import get_object_or_404

# app
from integrations.models import GoogleApi


def setup():
    main()


def get_creds():
    
    identifier = 'GOOGLE_CALENDAR'
    
    google_calendar_api = get_object_or_404(
        GoogleApi,
        identifier=identifier
    )
    
    result = {
        'client_secret': google_calendar_api.o_auth_2_client_secret_json,
        'token': google_calendar_api.o_auth_2_token_json,
    }

    return result


def set_new_token(token):
    
    identifier = 'GOOGLE_CALENDAR'
    
    google_calendar_api = get_object_or_404(
        GoogleApi,
        identifier=identifier
    )
    
    google_calendar_api.o_auth_2_token_json = token

    google_calendar_api.save()

    return google_calendar_api


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """
    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    client_secret = get_creds()['client_secret']
    
    client_config = json.loads(client_secret)

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
            flow = InstalledAppFlow.from_client_config(client_config, scopes=SCOPES,)

            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
