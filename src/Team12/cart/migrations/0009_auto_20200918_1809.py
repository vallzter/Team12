# Generated by Django 3.1.1 on 2020-09-18 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_customer'),
        ('cart', '0008_auto_20200918_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ship_to',
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
