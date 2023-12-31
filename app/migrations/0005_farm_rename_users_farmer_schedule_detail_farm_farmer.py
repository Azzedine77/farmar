# Generated by Django 4.2.4 on 2023-08-11 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sessions", "0001_initial"),
        ("app", "0004_alter_users_mobile_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="Farm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("area", models.FloatField()),
                ("village", models.CharField(max_length=255)),
                ("crop_grown", models.CharField(blank=True, max_length=255)),
                ("sowing_date", models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name="Users",
            new_name="Farmer",
        ),
        migrations.CreateModel(
            name="Schedule_detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("days_after_sowing", models.IntegerField()),
                ("Fertiliser", models.CharField(blank=True, max_length=255)),
                ("quantity", models.IntegerField()),
                (
                    "quantity_unit",
                    models.CharField(
                        choices=[
                            ("ton", "Ton"),
                            ("kg", "Kilograms"),
                            ("g", "grams"),
                            ("L", "litres"),
                            ("mL", "millitres"),
                        ],
                        max_length=10,
                    ),
                ),
                ("price", models.FloatField(default=0)),
                ("due_date", models.DateTimeField(null=True)),
                (
                    "farm",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.farm",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="farm",
            name="farmer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.farmer"
            ),
        ),
    ]
