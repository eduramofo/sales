from django.db import models
from core.models import BaseModel


class Event(BaseModel):

    summary = models.CharField(
        max_length=250,
        verbose_name='Resumo do Evento',
        null=False,
        blank=False,
    )

    start_datetime = models.DateTimeField(
        verbose_name='Início Data e Hora',
        null=True,
        blank=True,
    )

    end_datetime = models.DateTimeField(
        verbose_name='Fim Data e Hora',
        null=True,
        blank=True,
    )

    lead = models.ForeignKey(
        'leads.Lead',
        verbose_name='Associada ao Lead',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    done = models.BooleanField(
        verbose_name='Realizado?',
        default=False,
        null=False,
        blank=False,
    )

    account = models.ForeignKey(
        'account.Account',
        verbose_name='Dono',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    note = models.TextField(
        verbose_name='Anotações',
        null=True,
        blank=True,
    )

    google_calendar_calendar_id = models.CharField(
        verbose_name='Google Calendar: [calendarId]',
        max_length=500,
        null=True,
        blank=True,
    )

    google_calendar_event_id = models.CharField(
        verbose_name='Google Calendar: [eventId]',
        max_length=500,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-created_at']

    def __str__(self):
        result = str(self.id)
        if self.summary: return self.summary
        return  result
