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
    ("tentando_contato", "Tentando Contato"),
    # ("processando", "PROCESSANDO"),
    ("sem_interesse", "Sem Interesse"),
    ("sem_condicoes_financeiras", "Sem Dinheiro"),
    ("contato_invalido", "Contato Inválido"),
    # ("ignorando", "Rejeitando as Ligações"),
    ("agendamento", "Agendamento"),
    # ("acompanhamento", "ACOMPANHAMENTO"),
    ("ganho", "Ganho"),
    # ("perdido", "PERDIDO"),
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

    gmt = models.IntegerField(
        verbose_name='GMT',
        default=-3,
    )

    priority = models.BooleanField(
        verbose_name='Prioridade?',
        default=False,
    )

    location = models.CharField(
        max_length=1024,
        verbose_name='Localização: País/Cidade',
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

    run_now = models.BooleanField(
        verbose_name='Executar Agora?',
        default=False,
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


class Referrer(BaseModel):

    name = models.CharField(
        max_length=1024,
        verbose_name='Nome do Referenciador',
    )

    gmt = models.IntegerField(
        verbose_name='GMT',
        default=-3,
    )

    short_description = models.CharField(
        max_length=1024,
        verbose_name='Descrição curta da linha',
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=1024,
        verbose_name='Localização: País/Cidade',
        null=True,
        blank=True,
    )

    referring_datetime = models.DateTimeField(
        verbose_name='Data e hora da indicação',
        null=True,
        blank=True,
    )

    file_content_string = models.TextField(
        verbose_name='Conteúdo em (texto/string) do Arquivo',
        null=True,
        blank=True,
    )

    leads = models.ManyToManyField(
        'leads.Lead'
    )

    class Meta:
        verbose_name = "Referrer"
        verbose_name_plural = "Referrers"

    def __str__(self):
        if self.name: return str(self.name)
        else: return str(self.id)
