# Generated by Django 3.2.18 on 2023-06-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='total_reviews',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
