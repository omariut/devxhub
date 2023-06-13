# Generated by Django 3.2.18 on 2023-06-13 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_total_amount'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order', 'product'), name='unique_order_product'),
        ),
    ]
