# Generated by Django 4.2.3 on 2023-08-13 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0024_schedule_detail_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="schedule_detail",
            old_name="atmospheric_pressure_lowest",
            new_name="humidity_soil",
        ),
        migrations.RenameField(
            model_name="schedule_detail",
            old_name="humidity_soil_highest",
            new_name="humidity_weather",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="effect_of_atmospheric_pressure",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="effect_of_weather_humidity",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="humidity_soil_lowest",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="humidity_weather_highest",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="humidity_weather_lowest",
        ),
        migrations.RemoveField(
            model_name="schedule_detail", name="illumination_lowest",
        ),
    ]