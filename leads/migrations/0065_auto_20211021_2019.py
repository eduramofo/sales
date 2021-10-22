# Generated by Django 3.1.2 on 2021-10-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0064_auto_20211021_2000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linegrupo',
            options={'verbose_name': 'Grupo da Linha', 'verbose_name_plural': 'Grupo da Linhas'},
        ),
        migrations.AddField(
            model_name='linegrupo',
            name='default',
            field=models.BooleanField(default=False, verbose_name='Padrão?'),
        ),
    ]
