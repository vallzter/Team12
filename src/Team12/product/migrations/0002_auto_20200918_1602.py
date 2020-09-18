# Generated by Django 3.1.1 on 2020-09-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='image',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mealplan',
            name='ingredients',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='recipe',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
