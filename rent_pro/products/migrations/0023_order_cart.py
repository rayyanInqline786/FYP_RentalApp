# Generated by Django 3.2.7 on 2021-11-18 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_cart_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.cart'),
        ),
    ]
