import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from event.models import Event
from integrations.google_calendar import events


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Event)
def integrates_with_google_calendar(sender, instance, created, **kwargs):
    # on created
    if created:
        try:
            lead = instance.lead
            if lead:
                google_calendar_event = events.create(instance)
                if google_calendar_event['success']:
                    event_data = google_calendar_event['event']
                    event_data_event_id = event_data.get('id')
                    google_calendar_id = google_calendar_event['calendar_id']
                    instance.google_calendar_event_id = event_data_event_id
                    instance.google_calendar_calendar_id = google_calendar_id
                    instance.save()
        except Exception as error:
            logger.error(str(error))
    # on update
    else:
        try:
            lead = instance.lead
            if lead.status == 'agendamento':
                events.update(instance)
        except Exception as error:
            logger.error(str(error))
