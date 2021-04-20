# Generated by Django 3.1.2 on 2021-04-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0004_auto_20210416_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='googleapi',
            old_name='o_auth_2_json',
            new_name='o_auth_2_client_secret_json',
        ),
        migrations.AddField(
            model_name='googleapi',
            name='o_auth_2_token_json',
            field=models.TextField(blank=True, null=True, verbose_name='O Auth 2.0 JSON [ Token ]'),
        ),
    ]