# Generated by Django 3.1.2 on 2020-12-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0023_auto_20201213_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrer',
            name='short_description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Descrição curta da "linha"'),
        ),
    ]
