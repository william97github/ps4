# Generated by Django 4.1.6 on 2023-03-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secundario', '0004_alquiler_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='adicional',
            field=models.BooleanField(default=False),
        ),
    ]
