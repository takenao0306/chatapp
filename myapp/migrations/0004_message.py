# Generated by Django 5.0.2 on 2024-02-11 02:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_rename_customuser_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("message", models.CharField(max_length=1000)),
                (
                    "pub_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="レシーバー",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="センダー",
                    ),
                ),
            ],
        ),
    ]
