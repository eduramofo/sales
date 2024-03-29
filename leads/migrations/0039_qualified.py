# Generated by Django 3.1.2 on 2021-02-10 01:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0038_auto_20210121_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualified',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
                ('waid', models.CharField(blank=True, max_length=50, null=True, verbose_name='WhatsApp')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
