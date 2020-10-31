# Generated by Django 3.1.2 on 2020-10-29 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='quality',
            field=models.SmallIntegerField(default=0, verbose_name='Qualidade do Lead'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='tels',
            field=models.CharField(max_length=1024, verbose_name='Telefone de Contato'),
        ),
    ]
