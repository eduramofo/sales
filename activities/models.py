from django.db import models

from core.models import BaseModel


ACTIVITY_TYPE_CHOICES = (
    ("ligacao_normal", "Ligação Normal"),
    ("ligacao_whatsapp", "Ligação WhatsApp"),
    ("mensagem_whatsapp", "Mensagem WhatsApp"),
    ("audio_whatsapp", "Áudio WhatsApp"),
    ("reuniao", "Reunião"),
    ("Tarefa", "Tarefa"),
)

class Activity(BaseModel):

    type = models.CharField(
        max_length=120,
        verbose_name='Tipo',
        choices= ACTIVITY_TYPE_CHOICES,
        default='ligacao_normal',
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
        verbose_name='Data de Vencimento',
        null=True,
        blank=True,
    )

    note = models.TextField(
        verbose_name='Anotações',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"

    def __str__(self):

        if self.type and self.subject:
            return str(self.type) + " | " + str(self.subject)
        elif self.subject:
            return str(self.subject)
        elif self.type:
            return str(self.type)
        else:
            return str(self.id)
