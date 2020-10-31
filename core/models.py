import uuid
from django.db import models


class BaseModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Atualização',
    )

    class Meta:
        abstract = True
