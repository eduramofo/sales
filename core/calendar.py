import datetime

# google
from googleapiclient.discovery import build

# django
from django.conf import settings

# settings
API_KEY = settings.GOOGLE_CALENDAR_API_KEY_V1
CALENDAR_ID = settings.GOOGLE_CALENDAR_CALENDAR_ID

def setup():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    service = build('calendar', 'v3', developerKey=API_KEY)
    eventsResult = service.events().list(calendarId=CALENDAR_ID, timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
