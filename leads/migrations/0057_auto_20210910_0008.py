# Generated by Django 3.1.2 on 2021-09-10 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0056_whatsapptemplatecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapptemplatecategory',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
    ]
