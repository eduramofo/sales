from django.db import models

from core.models import BaseModel


class GoogleApi(BaseModel):

    description = models.CharField(
        max_length=120,
        verbose_name='Descrição',
        null=True,
        blank=True,
    )

    identifier = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Identificador',
    )

    o_auth_2_client_secret_json = models.TextField(
        verbose_name='O Auth 2.0 JSON [ Client Secret ]',
        null=True,
        blank=True,
    )

    o_auth_2_token_json = models.TextField(
        verbose_name='O Auth 2.0 JSON [ Token ]',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Google API"
        verbose_name_plural = "Google API's"

    def __str__(self):
        return self.description

