# Generated by Django 4.1.6 on 2023-03-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secundario', '0003_alter_alquiler_consola_alter_alquiler_mando_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
