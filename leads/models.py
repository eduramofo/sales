from django.db import models
from core.models import BaseModel


LEAD_QUALITY_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)

LEAD_STATUS_CHOICES = (
    ("novo", "NOVO"),
    ("tentando_contato", "TENTANDO CONTATO"),
    ("processando", "PROCESSANDO"),
    ("sem_interesse", "SEM INTERESSE"),
    ("contato_invalido", "CONTATO INVÁLIDO"),
    ("ignorando", "REJEITANDO AS LIGAÇÕES"),
    ("agendamento", "AGENDAMENTO"),
    ("acompanhamento", "ACOMPANHAMENTO"),
    ("ganho", "GANHO"),
    ("perdido", "PERDIDO"),
)

ACTIVITY_TYPE_CHOICES = (
    ("ligacao_normal", "Ligação Normal"),
    ("ligacao_whatsapp", "Ligação WhatsApp"),
    ("mensagem_whatsapp", "Mensagem WhatsApp"),
    ("audio_whatsapp", "Áudio WhatsApp"),
    ("reuniao", "Reunião"),
    ("Tarefa", "Tarefa"),
)


class Lead(BaseModel):

    status = models.CharField(
        max_length=50,
        verbose_name='Status',
        choices=LEAD_STATUS_CHOICES,
        default='novo',
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=1024,
        verbose_name='Nome',
    )

    indicated_by = models.CharField(
        max_length=1024,
        verbose_name='Indicado por',
        null=True,
        blank=True,
    )

    indicated_by_datetime = models.DateTimeField(
        verbose_name='Data e hora da indicação',
        null=True,
        blank=True,
    )

    tel = models.CharField(
        max_length=1024,
        verbose_name='Telefone',
        null=True,
        blank=True,
    )

    waid = models.CharField(
        max_length=1024,
        verbose_name='WhatsApp ID',
        null=True,
        blank=True,
    )

    quality = models.SmallIntegerField(
        verbose_name='Qualidade (1 - 5)',
        choices=LEAD_QUALITY_CHOICES,
        default=1,
    )

    next_contact = models.DateTimeField(
        verbose_name='Próximo contato',
        null=True,
        blank=True,
    )

    note = models.TextField(
        verbose_name='Anotações',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        if self.name and self.indicated_by:
            return str(self.name) + " | " + str(self.indicated_by)
        elif self.name:
            return str(self.name)
        else:
            return str(self.id)


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
