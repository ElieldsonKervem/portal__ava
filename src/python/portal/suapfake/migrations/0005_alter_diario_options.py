# Generated by Django 4.1.7 on 2023-04-10 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suapfake', '0004_alter_diario_pacote_enviado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diario',
            options={'ordering': ['id'], 'verbose_name': 'diário fake', 'verbose_name_plural': 'diários fake'},
        ),
    ]
