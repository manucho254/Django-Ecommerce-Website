# Generated by Django 3.2 on 2021-05-03 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cart_cartitems'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.DeleteModel(
            name='cartItems',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
