# Generated by Django 5.0.6 on 2024-06-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='descricao',
            field=models.TextField(default='Descrição padrão'),
        ),
        migrations.AddField(
            model_name='subgrupo',
            name='descricao',
            field=models.TextField(default='Descrição padrão'),
        ),
    ]
