# Generated by Django 3.1.2 on 2021-10-22 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211022_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='current_line_group_activated',
            new_name='current_line_group',
        ),
    ]