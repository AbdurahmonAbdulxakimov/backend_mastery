# Generated by Django 4.2.7 on 2024-04-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estate", "0002_alter_estate_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estate",
            name="price",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
