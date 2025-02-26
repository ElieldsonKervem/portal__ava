# Generated by Django 4.0.4 on 2022-06-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suapfake', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diario',
            options={'ordering': ['id'], 'verbose_name': 'diário', 'verbose_name_plural': 'diários'},
        ),
        migrations.RemoveField(
            model_name='diario',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='diario',
            name='suap_id',
        ),
        migrations.AlterField(
            model_name='diario',
            name='pacote_enviado',
            field=models.JSONField(verbose_name='pacote a enviar/enviado'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='pacote_recebido',
            field=models.JSONField(blank=True, null=True, verbose_name='pacote recebido'),
        ),
    ]
