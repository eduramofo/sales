# Generated by Django 3.1.2 on 2021-10-21 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0059_auto_20211020_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='best_time_to_contact',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Melhor horário para contato'),
        ),
    ]
