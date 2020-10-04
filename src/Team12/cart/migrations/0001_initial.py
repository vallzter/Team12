# Generated by Django 3.1.1 on 2020-10-04 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Ceation date')),
                ('web_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_owner', to=settings.AUTH_USER_MODEL, verbose_name='Web User')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.DateField(auto_now_add=True, verbose_name='Order date')),
                ('shipped', models.DateField(verbose_name='Shipping date')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
                ('total', models.IntegerField(verbose_name='Total')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=16, verbose_name='Card number')),
                ('CVV', models.CharField(max_length=4, verbose_name='Card Verification Value')),
                ('date', models.DateField(verbose_name='Expiration date')),
                ('name', models.CharField(max_length=50, verbose_name='Cardholder name')),
            ],
            options={
                'verbose_name': 'PaymentMethod',
                'verbose_name_plural': 'PaymentMethods',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('region', models.CharField(max_length=50, verbose_name='Region/State')),
                ('city', models.IntegerField(verbose_name='Postcode')),
                ('street', models.CharField(max_length=50, verbose_name='Street address')),
                ('info', models.CharField(max_length=50, verbose_name='Additional info')),
            ],
            options={
                'verbose_name': 'shippingaddress',
                'verbose_name_plural': "shippingaddress'",
            },
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Cart')),
                ('mealplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mealplan', verbose_name='')),
            ],
            options={
                'verbose_name': 'lineitem',
                'verbose_name_plural': 'lineitems',
            },
        ),
    ]
