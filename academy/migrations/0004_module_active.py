# Generated by Django 3.1.2 on 2021-09-07 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]