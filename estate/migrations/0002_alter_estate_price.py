# Generated by Django 4.2.7 on 2024-04-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estate", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estate",
            name="price",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
