# Generated by Django 4.2.3 on 2023-08-12 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0020_alter_farmer_mobile_number"),
    ]

    operations = [
        migrations.RemoveField(model_name="schedule_detail", name="Fertiliser",),
        migrations.RemoveField(model_name="schedule_detail", name="quantity",),
        migrations.RemoveField(model_name="schedule_detail", name="quantity_unit",),
        migrations.RemoveField(model_name="schedule_detail", name="types",),
        migrations.AddField(
            model_name="schedule_detail",
            name="The_highest_appropriate_temperature",
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="The_lowest_appropriate_temperature",
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="atmospheric_pressure_highest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="atmospheric_pressure_lowest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="effect_of_atmospheric_pressure",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="effect_of_heat",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="effect_of_illumination",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="effect_of_soil_humidity",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="effect_of_weather_humidity",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="humidity_soil_highest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="humidity_soil_lowest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="humidity_weather_highest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="humidity_weather_lowest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="illumination_highest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="schedule_detail",
            name="illumination_lowest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="schedule_detail",
            name="farm",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.farm",
            ),
        ),
    ]
