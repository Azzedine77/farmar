# Generated by Django 4.2.4 on 2023-08-12 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0016_remove_category_category_remove_farmer_token_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="farmer",
            name="business_manager_name",
        ),
        migrations.AddField(
            model_name="farmer",
            name="detiel",
            field=models.TextField(blank=True, null=True, verbose_name="detiel"),
        ),
    ]
