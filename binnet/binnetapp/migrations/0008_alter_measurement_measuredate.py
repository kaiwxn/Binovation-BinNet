# Generated by Django 5.0.2 on 2024-03-17 11:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binnetapp', '0007_remove_measurement_date_measurement_measuredate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measureDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
