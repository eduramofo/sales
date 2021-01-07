# Generated by Django 3.1.2 on 2021-01-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0031_whatsapptemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='status_lost_justification',
            field=models.CharField(blank=True, choices=[('sem_interesse', 'Sem Interesse'), ('sem_dinheiro', 'Sem Dinheiro'), ('ja_estuda_ingles', 'Já Estuda Inglês'), ('ja_fala_ingles', 'Já Fala Inglês'), ('invalido', 'contato_invalido'), ('duplicado', 'Duplicado'), ('ignorando', 'Ignorando'), ('bloqueado', 'Bloqueado'), ('outro', 'Outro')], max_length=300, null=True, verbose_name='Justificativa da Perda'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='quality',
            field=models.SmallIntegerField(choices=[(1, '1')], default=1, verbose_name='Qualidade (1 - 5)'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='short_description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Descrição curta da (linha)'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('novo', 'Novo'), ('tentando_contato', 'Tentando Contato'), ('agendamento', 'Agendamento'), ('ganho', 'Ganho'), ('perdido', 'Perdido'), ('sem_interesse', 'Sem Interesse'), ('sem_condicoes_financeiras', 'Sem Dinheiro'), ('contato_invalido', 'Contato Inválido')], default='novo', max_length=50, verbose_name='Status'),
        ),
    ]
