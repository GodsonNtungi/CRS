# Generated by Django 4.1.7 on 2023-04-27 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Crop",
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
                ("name", models.CharField(max_length=20)),
                ("N", models.PositiveIntegerField(default=0)),
                ("K", models.PositiveIntegerField(default=0)),
                ("humidity", models.PositiveIntegerField(default=0)),
                ("temperature", models.PositiveIntegerField(default=0)),
                ("ph", models.PositiveIntegerField(default=0)),
                ("rainfall", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=20)),
                (
                    "crop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="crop_location",
                        to="app.crop",
                    ),
                ),
            ],
        ),
    ]
