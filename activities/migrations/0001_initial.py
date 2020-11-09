# Generated by Django 3.1.2 on 2020-11-09 05:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
                ('type', models.CharField(choices=[('ligacao_normal', 'Ligação Normal'), ('ligacao_whatsapp', 'Ligação WhatsApp'), ('mensagem_whatsapp', 'Mensagem WhatsApp'), ('audio_whatsapp', 'Áudio WhatsApp'), ('reuniao', 'Reunião'), ('Tarefa', 'Tarefa')], default='ligacao_normal', max_length=120, verbose_name='Tipo')),
                ('subject', models.CharField(max_length=250, verbose_name='Assunto')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de Vencimento')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Anotações')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
    ]
