# Generated by Django 4.2.3 on 2023-08-13 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "app",
            "0025_rename_atmospheric_pressure_lowest_schedule_detail_humidity_soil_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="schedule_detail",
            old_name="The_highest_appropriate_temperature",
            new_name="The_appropriate_temperature",
        ),
        migrations.RenameField(
            model_name="schedule_detail",
            old_name="atmospheric_pressure_highest",
            new_name="atmospheric_pressure",
        ),
        migrations.RenameField(
            model_name="schedule_detail",
            old_name="illumination_highest",
            new_name="illumination",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="The_lowest_appropriate_temperature",
        ),
        migrations.RemoveField(model_name="schedule_detail", name="effect_of_heat",),
        migrations.RemoveField(
            model_name="schedule_detail", name="effect_of_illumination",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="effect_of_soil_humidity",
        ),
        migrations.RemoveField(model_name="schedule_detail", name="name",),
    ]
