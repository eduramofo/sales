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
