# Generated by Django 3.1.2 on 2021-04-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0048_auto_20210408_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='nickname',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Apelido'),
        ),
    ]
