from django.db import models

from core.models import BaseModel


ACTIVITY_TYPE_CHOICES = (
    ('call', 'Ligação'),
    ('whatsapp_message', 'WhatsApp Mensagem'),
    ('whatsapp_audio', 'WhatsApp Áudio'),
    ('presentation', 'Apresentação'),
)

class Activity(BaseModel):

    type = models.CharField(
        max_length=120,
        verbose_name='Tipo',
        choices= ACTIVITY_TYPE_CHOICES,
        default='call',
        null=False,
        blank=False,
    )

    subject = models.CharField(
        max_length=250,
        verbose_name='Assunto',
        null=False,
        blank=False,
    )

    due_date = models.DateTimeField(
        verbose_name='Data/Hora',
        null=True,
        blank=True,
    )

    done = models.BooleanField(
        verbose_name='Feita?',
        default=False,
        null=False,
        blank=False,
    )

    note = models.TextField(
        verbose_name='Anotações',
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

    account = models.ForeignKey(
        'account.Account',
        verbose_name='Dono',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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

    notification_sent = models.BooleanField(
        verbose_name='Notificação Enviada',
        default=False,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ['-created_at']

    def __str__(self):

        if self.type and self.subject:
            return str(self.type) + " | " + str(self.subject)
        elif self.subject:
            return str(self.subject)
        elif self.type:
            return str(self.type)
        else:
            return str(self.id)
