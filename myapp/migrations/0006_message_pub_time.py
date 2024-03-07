# Generated by Django 5.0.2 on 2024-02-11 07:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_remove_message_pub_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="pub_time",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="作成日時",
            ),
            preserve_default=False,
        ),
    ]
