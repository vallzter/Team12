# Generated by Django 3.1.1 on 2020-09-18 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20200918_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitem',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
