# Generated by Django 5.0.2 on 2024-03-17 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binnetapp', '0006_rename_lat_bin_latitude_rename_lon_bin_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='date',
        ),
        migrations.AddField(
            model_name='measurement',
            name='measureDate',
            field=models.DateField(default=datetime.date(2024, 3, 17)),
        ),
        migrations.AddField(
            model_name='measurement',
            name='measureTime',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]