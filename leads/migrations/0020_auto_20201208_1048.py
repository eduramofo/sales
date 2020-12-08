# Generated by Django 3.1.2 on 2020-12-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_delete_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('novo', 'Novo'), ('tentando_contato', 'Tentando Contato'), ('sem_interesse', 'Sem Interesse'), ('sem_condicoes_financeiras', 'Sem Dinheiro'), ('contato_invalido', 'Contato Inválido'), ('agendamento', 'Agendamento'), ('ganho', 'Ganho')], default='novo', max_length=50, verbose_name='Status'),
        ),
    ]
