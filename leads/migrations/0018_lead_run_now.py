# Generated by Django 3.1.2 on 2020-11-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_auto_20201107_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='run_now',
            field=models.BooleanField(default=False, verbose_name='Executar Agora?'),
        ),
    ]
