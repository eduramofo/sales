from django.db import models
from core.models import BaseModel


class Conversation(BaseModel):

    CONVERSATION_SEM_INTERESSE = 'sem_interesse'
    CONVERSATION_AGENDAMENTO = 'agendamento'
    CONVERSATION_DI = 'di'
    CONVERSATION_LOST = 'lost'
    CONVERSATION_WIN = 'win'
    CONVERSATION_OFF = 'off'

    CONVERSATION_TYPE_CHOICES = (
        (CONVERSATION_SEM_INTERESSE, 'Sem Interesse'),
        (CONVERSATION_AGENDAMENTO, 'Agendamento'),
        (CONVERSATION_DI, 'DI'),
        (CONVERSATION_LOST, 'Entrevista Perdida'),
        (CONVERSATION_WIN, 'Entrevista Ganha'),
        (CONVERSATION_OFF, 'Entrevista Off'),
    )

    type = models.CharField(
        max_length=120,
        verbose_name='Tipo de Conversa',
        choices= CONVERSATION_TYPE_CHOICES,
        null=False,
        blank=False,
    )

    lead = models.ForeignKey(
        'leads.Lead',
        verbose_name='Associada ao Lead',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Conversa"
        verbose_name_plural = "Conversas"
        ordering = ['-created_at']

    def __str__(self):
        if self.type:
            return self.type
        else:
            return str(self.id)
