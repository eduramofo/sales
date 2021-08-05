# Generated by Django 3.1.2 on 2021-08-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0005_auto_20210416_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='googleapi',
            name='o_auth_2_credentials_client_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Credentials [ client_id ]'),
        ),
        migrations.AddField(
            model_name='googleapi',
            name='o_auth_2_credentials_client_secret',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Credentials [ client_secret ]'),
        ),
        migrations.AddField(
            model_name='googleapi',
            name='o_auth_2_credentials_refresh_token',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Credentials [ refresh_token ]'),
        ),
        migrations.AddField(
            model_name='googleapi',
            name='o_auth_2_credentials_scopes',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Credentials [ scopes ]'),
        ),
        migrations.AddField(
            model_name='googleapi',
            name='o_auth_2_credentials_token',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Credentials [ token ]'),
        ),
        migrations.AddField(
            model_name='googleapi',
            name='o_auth_2_credentials_token_uri',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Credentials [ token_uri ]'),
        ),
    ]