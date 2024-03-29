# Generated by Django 3.1.2 on 2020-10-29 03:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
                ('name', models.CharField(max_length=1024, verbose_name='Nome do contato')),
                ('tels', models.CharField(max_length=1024, verbose_name='Telefone do Contato')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
