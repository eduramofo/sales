# Generated by Django 3.1.2 on 2020-12-13 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0025_auto_20201213_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referrer',
            name='leads',
        ),
    ]