# Generated by Django 3.1.2 on 2021-04-16 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='googleapi',
            options={'verbose_name': 'Google API', 'verbose_name_plural': "Google API's"},
        ),
    ]