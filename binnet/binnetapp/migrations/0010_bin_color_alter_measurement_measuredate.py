# Generated by Django 5.0.2 on 2024-03-24 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binnetapp', '0009_alter_measurement_measuredate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='color',
            field=models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('G', 'Green'), ('B', 'DEFAULT')], default='B', max_length=7),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measureDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 24, 10, 7, 58, 498429, tzinfo=datetime.timezone.utc)),
        ),
    ]
