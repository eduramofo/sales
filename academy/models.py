from django.db import models
from core.models import BaseModel


class AudioSpeech(BaseModel):

    active = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Ordem',
        default=1,
        null=True,
        blank=False,
    )

    name = models.CharField(
        max_length=500,
        verbose_name='Nome',
        null=True,
        blank=False,
    )

    audio_file = models.FileField(
        verbose_name='Arquivo do Áudio do Speech',
        upload_to='academy/audio-speech/',
        null=True,
        blank=False,
    )

    class Meta:
        verbose_name = 'Áudio de Entrevista'
        verbose_name_plural = 'Áudios de Entrevistas'
        ordering = ('-order',)


    def __str__(self):
        result = str(self.id)
        if self.name:
            result = str(self.name)
        return result


class Module(BaseModel):
    
    active = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )

    title = models.CharField(
        max_length=500,
        verbose_name='Título',
        null=True,
        blank=False,
    )

    url = models.SlugField(
        verbose_name='URL',
        unique=True,
        null=True,
        blank=False,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Ordem',
        default=1,
        null=True,
        blank=False,
    )

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ('order',)


    def __str__(self):
        result = str(self.id)
        if self.title: result = str(self.title)
        return result

    def get_submodules(self):
        return Submodule.objects.filter(module=self, active=True)


class Submodule(BaseModel):

    active = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )

    title = models.CharField(
        max_length=500,
        verbose_name='Título',
        null=True,
        blank=False,
    )

    url = models.SlugField(
        verbose_name='URL',
        unique=True,
        null=True,
        blank=False,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Ordem',
        default=1,
        null=True,
        blank=False,
    )

    module = models.ForeignKey(
        'academy.Module',
        verbose_name='Módulo',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Submódulo'
        verbose_name_plural = 'Submódulo'
        ordering = ('order',)


    def __str__(self):
        result = str(self.id)
        if self.title: result = str(self.title)
        return result
