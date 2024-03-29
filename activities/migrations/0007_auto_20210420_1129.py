# Generated by Django 3.1.2 on 2021-04-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_activity_notification_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='google_calendar_calendar_id',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Google Calendar: [calendarId]'),
        ),
        migrations.AddField(
            model_name='activity',
            name='google_calendar_event_id',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Google Calendar: [eventId]'),
        ),
    ]
