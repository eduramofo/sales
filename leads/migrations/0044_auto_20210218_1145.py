# Generated by Django 3.1.2 on 2021-02-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0043_auto_20210218_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status_lost_justification',
            field=models.CharField(blank=True, choices=[('', 'Selecionar'), ('sem_interesse', 'Sem interesse'), ('nao_e_prioridade', 'Não é prioridade'), ('sem_dinheiro', 'Sem dinheiro'), ('ja_estuda_ingles', 'Já estuda inglês'), ('ja_fala_ingles', 'Já fala inglês'), ('nao_gosta_de_ead', 'Não gosta de EAD'), ('nao_gosta_de_ingles', 'Não gosta de inglês'), ('invalido', 'Inválido'), ('duplicado', 'Duplicado'), ('ignorando', 'Ignorando'), ('agendamento_bolo', 'Bolo após o agendamento'), ('bloqueado', 'Bloqueado'), ('desligou_na_cara', 'Desligou na cara'), ('rejeitando', 'Rejeitando'), ('outro', 'Outro')], max_length=300, null=True, verbose_name='Justificativa da Perda'),
        ),
    ]
