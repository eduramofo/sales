# Generated by Django 3.1.2 on 2021-04-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0049_lead_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status_lost_justification',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Justificativa da Perda'),
        ),
    ]
