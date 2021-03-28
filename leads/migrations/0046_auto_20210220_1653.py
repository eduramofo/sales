# Generated by Django 3.1.2 on 2021-02-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0045_auto_20210218_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('novo', '1º Ligação (Novo)'), ('tentando_contato', '2º Ligação (Áudio)'), ('tentando_contato_2', '3º Ligação (Ultimado)'), ('agendamento', 'Agendamento'), ('acompanhamento', 'Follow-up'), ('geladeira', 'Geladeira'), ('perdido', 'Perdido'), ('ganho', 'Ganho')], default='novo', max_length=50, verbose_name='Status'),
        ),
    ]