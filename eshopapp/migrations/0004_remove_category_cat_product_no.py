# Generated by Django 4.0.3 on 2023-11-28 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshopapp', '0003_product_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat_product_no',
        ),
    ]
