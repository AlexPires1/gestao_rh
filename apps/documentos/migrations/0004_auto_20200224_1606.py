# Generated by Django 3.0.3 on 2020-02-24 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0010_funcionario_empresa'),
        ('documentos', '0003_documentos_arquivo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Documentos',
            new_name='Documento',
        ),
    ]