# Generated by Django 3.1.2 on 2021-10-22 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0068_auto_20211021_2339'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='active_line_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LineGroup', to='leads.linegroup', verbose_name='Grupo da Linha'),
        ),
    ]
