# Generated by Django 4.1.7 on 2023-04-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4', '0003_alter_usuario_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='email_escolar',
            new_name='email_google_classroom',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nome_apresentacao',
            new_name='nome_usual',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nome_civil',
            new_name='nome_registro',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='tipo',
            new_name='tipo_usuario',
        ),

        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(blank=True, max_length=255, verbose_name='nome no SUAP'),
        ),

        migrations.AlterField(
            model_name='usuario',
            name='nome_social',
            field=models.CharField(blank=True, max_length=255, verbose_name='nome social'),
        ),

    ]
