from django.db import models
from django.utils import timezone

from core.models import BaseModel


LEAD_QUALITY_CHOICES = (
    (1, '1'),
)

LEAD_STATUS_CHOICES = (
    ('novo', 'Novo - T1'),
    ('tentando_contato', 'Tentando - T2'),
    ('tentando_contato_2', 'Ultimato - T3'),
    ('geladeira', 'Geladeira'),
    ('agendamento', 'Agendamento'),
    ('ghosting', 'Bolo 1'),
    ('ghosting_2', 'Bolo 2'),
    ('perdido', 'Perdido'),
    ('ganho', 'Ganho'),
    ('invalid', 'Inválido'),
    ('ultimatum', 'Ultimato'),
)

LEAD_GENDER_CHOICES = (
    ('f', 'Feminino'),
    ('m', 'Masculino'),
    ('o', 'Outros'),
)

BEST_TIME_CHOICES = (
    (None, 'Selecionar'),
    (1, 'Manhã'),
    (2, 'Tarde'),
    (3, 'Noite'),
)

LEAD_STATUS_LOST_JUSTIFICATION_CHOICES = (
    ('', 'Selecionar'),
    ('sem_interesse', 'Sem interesse'),
    ('nao_e_prioridade', 'Não é prioridade'),
    ('sem_dinheiro', 'Sem dinheiro'),
    ('sem_cartao_credito', 'Sem cartão crédito'),
    ('ja_estuda_ingles', 'Já estuda inglês'),
    ('ja_fala_ingles', 'Já fala inglês'),
    ('nao_gosta_de_ead', 'Não gosta de EAD'),
    ('nao_gosta_de_ingles', 'Não gosta de inglês'),
    ('invalido', 'Inválido'),
    ('duplicado', 'Duplicado'),
    ('ignorando', 'Ignorando'),
    ('agendamento_bolo', 'Bolo agendamento'),
    ('bloqueado', 'Bloqueado'),
    ('desligou_na_cara', 'Desligou na cara'),
    ('rejeitando', 'Rejeitando'),
    ('lost_direct', 'lost_direct'),
    ('outro', 'Outro'),
)


GMT_CHOICES = (
    (None, 'Selecionar'),
    (-1, 'GMT-1'),
    (-2, 'GMT-2'),
    (-3, 'GMT-3'),
    (-4, 'GMT-4'),
    (-5, 'GMT-5'),
    (-6, 'GMT-6'),
    (-7, 'GMT-7'),
    (-8, 'GMT-8'),
    (-9, 'GMT-9'),
    (-10, 'GMT-10'),
    (-11, 'GMT-11'),
    (-12, 'GMT-12'),
    (0, 'GMT'),
    (1, 'GMT+1'),
    (2, 'GMT+2'),
    (3, 'GMT+3'),
    (4, 'GMT+4'),
    (5, 'GMT+5'),
    (6, 'GMT+6'),
    (7, 'GMT+7'),
    (8, 'GMT+8'),
    (9, 'GMT+9'),
    (10, 'GMT+10'),
    (11, 'GMT+11'),
    (12, 'GMT+12'),
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

    status_lost_justification = models.CharField(
        max_length=300,
        # choices=LEAD_STATUS_LOST_JUSTIFICATION_CHOICES,
        verbose_name='Justificativa da Perda',
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=1024,
        verbose_name='Nome',
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Ordem',
        default=1,
    )

    nickname = models.CharField(
        max_length=1024,
        verbose_name='Apelido',
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=50,
        verbose_name='Sexo',
        choices=LEAD_GENDER_CHOICES,
        default='m',
        null=False,
        blank=False,
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

    # https://greenwichmeantime.com/cities/
    gmt = models.IntegerField(
        verbose_name='GMT',
        choices=GMT_CHOICES,
        default=-3,
    )

    qualified = models.BooleanField(
        verbose_name='Qualificado?',
        default=False,
    )

    priority = models.BooleanField(
        verbose_name='Prioridade?',
        default=False,
    )

    location = models.CharField(
        max_length=300,
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

    short_description = models.CharField(
        max_length=1024,
        verbose_name='Descrição curta da (linha)',
        null=True,
        blank=True,
    )

    def get_referrer(self):
        referrer_obj = Referrer.objects.filter(leads=self).first()
        if referrer_obj:
            return referrer_obj
        return None

    def get_referrer_name(self):
        referrer_obj = Referrer.objects.filter(leads=self).first()
        if referrer_obj:
            referrer_obj_lead = referrer_obj.lead
            if referrer_obj_lead:
                return referrer_obj_lead
            return referrer_obj.name
        return None

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self):
        if self.name and self.indicated_by:
            return str(self.name) + " | " + str(self.indicated_by)
        elif self.name:
            return str(self.name)
        else:
            return str(self.id)


class WhatsappTemplate(BaseModel):

    active = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Ordem',
        unique=True,
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=150,
        verbose_name='Nome',
        unique=True,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Título',
        null=True,
        blank=True,
    )

    content = models.CharField(
        max_length=1024,
        verbose_name='Conteúdo do template',
    )

    class Meta:
        verbose_name = 'Modelo de Mensagem para WhatsApp'
        verbose_name_plural = 'Modelos de Mensagens para WhatsApp'
        ordering = ['order']

    def __str__(self):
        return self.name


class Referrer(BaseModel):

    name = models.CharField(
        max_length=1024,
        verbose_name='Nome do Referenciador',
        null=True,
        blank=True,
    )

    lead = models.ForeignKey(
        'leads.Lead',
        verbose_name='Lead/Referenciador',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    gmt = models.IntegerField(
        verbose_name='GMT',
        default=-3,
        null=True,
        blank=True,
    )

    short_description = models.CharField(
        max_length=1024,
        verbose_name='Descrição curta da "linha"',
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

    leads = models.ManyToManyField('leads.Lead', 
        related_name='leads',
    )

    file_content_string = models.TextField(
        verbose_name='Conteúdo em (texto/string) do Arquivo',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Referenciador"
        verbose_name_plural = "Referenciadores"

    def __str__(self):

        result = str(self.id)

        if self.name:
            result = str(self.name)

        lead = self.lead
        if lead:
            result = str(self.lead)

        return result


class Qualified(BaseModel):

    name = models.CharField(
        max_length=500,
        verbose_name='Nome',
        null=True,
        blank=True,
    )

    waid = models.CharField(
        max_length=50,
        verbose_name='WhatsApp',
        null=True,
        blank=True,
    )

    processed = models.BooleanField(
        verbose_name='Processado?',
        default=False,
    )

    class Meta:
        verbose_name = 'Qualificado'
        verbose_name_plural = 'Qualificados'
        ordering = ('-created_at',)


    def __str__(self):
        result = str(self.id)
        if self.name:
            result = str(self.name)
        return result
