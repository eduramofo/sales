# Generated by Django 3.1.2 on 2021-08-06 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('leads', '0053_auto_20210716_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='referrer',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='Dono'),
        ),
    ]
