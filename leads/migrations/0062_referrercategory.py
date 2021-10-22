# Generated by Django 3.1.2 on 2021-10-21 22:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('leads', '0061_auto_20211021_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferrerCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
                ('active', models.BooleanField(default=False, verbose_name='Ativo?')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da Categoria')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='Dono')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
