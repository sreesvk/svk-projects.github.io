# Generated by Django 4.2.7 on 2023-12-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eshopapp", "0010_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="list_id",
            field=models.CharField(max_length=255, null=True),
        ),
    ]