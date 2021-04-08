# Generated by Django 3.1.2 on 2021-04-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0047_auto_20210221_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='gender',
            field=models.CharField(choices=[('f', 'Feminino'), ('m', 'Masculino'), ('o', 'Outros')], default='m', max_length=50, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('novo', 'Novo - T1'), ('tentando_contato', 'Tentando - T2'), ('tentando_contato_2', 'Ultimato - T3'), ('geladeira', 'Geladeira'), ('agendamento', 'Agendamento'), ('perdido', 'Perdido'), ('ganho', 'Ganho')], default='novo', max_length=50, verbose_name='Status'),
        ),
    ]
