# Generated by Django 3.1.2 on 2021-01-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0034_whatsapptemplate_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsapptemplate',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
    ]
