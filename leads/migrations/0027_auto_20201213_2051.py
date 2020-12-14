# Generated by Django 3.1.2 on 2020-12-13 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0026_remove_referrer_leads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrer',
            name='lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.lead', verbose_name='Lead/Referenciador'),
        ),
    ]
