# Generated by Django 5.0.6 on 2024-07-08 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_trainer_tarifa_alter_trainer_experiencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='experiencia',
        ),
        migrations.AddField(
            model_name='trainer',
            name='experiencia_anios',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]