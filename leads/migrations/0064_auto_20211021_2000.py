# Generated by Django 3.1.2 on 2021-10-21 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('leads', '0063_auto_20211021_1957'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReferrerCategory',
            new_name='LineGrupo',
        ),
    ]
