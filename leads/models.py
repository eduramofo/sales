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
    ("novo", "Novo"),
    ("processando", "Processando"),
    ("sem_interesse", "Contato realizado [ SEM INTERESSE ]"),
    ("contato_invalido", "Contato inválido"),
    ("ignorando", "Está rejeitando os contatos"),
    ("agendamento", "Agendamento"),
    ("acompanhamento", "Acompanhamento"),
    ("ganho", "Apresentação realizada [ GANHO ]"),
    ("perdido", "Apresentação realizada [ PERDIDO ]"),
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
