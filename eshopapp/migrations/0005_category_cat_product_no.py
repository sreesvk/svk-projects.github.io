# Generated by Django 4.0.3 on 2023-11-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopapp', '0004_remove_category_cat_product_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_product_no',
            field=models.IntegerField(null=True),
        ),
    ]
