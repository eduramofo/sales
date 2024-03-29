# Generated by Django 3.1.2 on 2020-12-08 20:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0020_auto_20201208_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='gmt',
            field=models.IntegerField(default=-3, verbose_name='GMT'),
        ),
        migrations.AddField(
            model_name='lead',
            name='location',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Localização: País/Cidade'),
        ),
        migrations.AddField(
            model_name='lead',
            name='priority',
            field=models.BooleanField(default=False, verbose_name='Prioridade?'),
        ),
        migrations.CreateModel(
            name='Referrer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
                ('name', models.CharField(max_length=1024, verbose_name='Nome do Referenciador')),
                ('gmt', models.IntegerField(default=-3, verbose_name='GMT')),
                ('short_description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Descrição curta da linha')),
                ('location', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Localização: País/Cidade')),
                ('referring_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Data e hora da indicação')),
                ('file_content_string', models.TextField(blank=True, null=True, verbose_name='Conteúdo em (texto/string) do Arquivo')),
                ('leads', models.ManyToManyField(to='leads.Lead')),
            ],
            options={
                'verbose_name': 'Referrer',
                'verbose_name_plural': 'Referrers',
            },
        ),
    ]
