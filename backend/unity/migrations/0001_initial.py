# Generated by Django 4.1.2 on 2022-10-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscriber",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_subscribed", models.BooleanField(default=False)),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
