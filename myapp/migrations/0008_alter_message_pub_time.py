# Generated by Django 5.0.2 on 2024-02-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_alter_message_pub_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="pub_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
        ),
    ]
