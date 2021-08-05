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

    calendar_id = models.CharField(
        max_length=250,
        verbose_name='Calendar ID',
        null=True,
        blank=True,
    )

    o_auth_2_client_secret_json = models.TextField(
        verbose_name='O Auth 2.0 JSON [ Client Secret ]',
        null=True,
        blank=True,
    )

    o_auth_2_credentials_token = models.CharField(
        max_length=500,
        verbose_name='Credentials [ token ]',
        null=True,
        blank=True,
    )

    o_auth_2_credentials_refresh_token = models.CharField(
        max_length=500,
        verbose_name='Credentials [ refresh_token ]',
            null=True,
        blank=True,
    )

    o_auth_2_credentials_token_uri = models.CharField(
        max_length=500,
        verbose_name='Credentials [ token_uri ]',
        null=True,
        blank=True,
    )

    o_auth_2_credentials_client_id = models.CharField(
        max_length=500,
        verbose_name='Credentials [ client_id ]',
        null=True,
        blank=True,
    )

    o_auth_2_credentials_client_secret = models.CharField(
        max_length=500,
        verbose_name='Credentials [ client_secret ]',
        null=True,
        blank=True,
    )

    o_auth_2_credentials_scopes = models.CharField(
        max_length=500,
        verbose_name='Credentials [ scopes ]',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Google API"
        verbose_name_plural = "Google API's"

    def __str__(self):
        return self.description
