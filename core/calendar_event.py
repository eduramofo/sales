API_KEY = settings.GOOGLE_CALENDAR_API_KEY_V1
CALENDAR_ID = settings.GOOGLE_CALENDAR_API_CALENDAR_ID

# books_service = build('books', 'v1', developerKey=API_KEY)

event = {
  'summary': 'João Pedro',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2021-04-15T16:00:00-03:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2021-04-28T17:00:00-03:00',
    'timeZone': 'America/Sao_Paulo',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'popup', 'minutes': 3},
    ],
  },
}

event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
print 'Event created: %s' % (event.get('htmlLink'))
