# Generated by Django 4.2.4 on 2023-08-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0011_type_effect_of_heat_type_effect_of_humidity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="type",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ton", "Ton"),
                    ("kg", "Kilograms"),
                    ("g", "grams"),
                    ("L", "litres"),
                    ("mL", "millitres"),
                ],
                help_text="Select type:",
                max_length=50,
                null=True,
                verbose_name="Type",
            ),
        ),
    ]
