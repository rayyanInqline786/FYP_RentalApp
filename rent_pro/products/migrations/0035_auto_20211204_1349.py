# Generated by Django 3.2.7 on 2021-12-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_alter_product_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='your_bid_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='your_bid_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
