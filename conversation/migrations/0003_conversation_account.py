# Generated by Django 3.1.2 on 2021-08-18 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('conversation', '0002_auto_20210716_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='Dono'),
        ),
    ]
