# Generated by Django 3.1.2 on 2020-11-10 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Feita?'),
        ),
    ]
