# Generated by Django 3.1.2 on 2021-07-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='type',
            field=models.CharField(choices=[('sem_interesse', 'Sem Interesse'), ('agendamento', 'Agendamento'), ('di', 'DI'), ('lost', 'Entrevista Perdida'), ('win', 'Entrevista Ganha'), ('off', 'Entrevista Off')], max_length=120, verbose_name='Tipo de Conversa'),
        ),
    ]
