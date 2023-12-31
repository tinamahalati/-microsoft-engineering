# Generated by Django 4.1.7 on 2023-05-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("national_id", models.CharField(max_length=10)),
                ("phone_number", models.CharField(max_length=12)),
                ("gym_id", models.CharField(max_length=14)),
            ],
        ),
    ]
