# Generated by Django 3.0.3 on 2020-02-24 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0010_funcionario_empresa'),
        ('documentos', '0004_auto_20200224_1606'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Documento',
            new_name='Documentos',
        ),
    ]
