# Generated by Django 3.1.2 on 2021-08-06 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('leads', '0054_referrer_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='Dono'),
        ),
    ]
