# Generated by Django 3.1.2 on 2021-08-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0009_auto_20210805_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleapi',
            name='calendar_id',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Calendar ID'),
        ),
    ]
