# Generated by Django 4.2.4 on 2023-08-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0017_remove_farmer_business_manager_name_farmer_detiel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farmer",
            name="organization_name",
            field=models.CharField(max_length=50, verbose_name="Farm Name"),
        ),
    ]