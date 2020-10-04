# Generated by Django 3.1.1 on 2020-10-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('recipe', models.TextField()),
                ('ingredients', models.TextField(default='N/A')),
                ('image', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'meal plan',
                'verbose_name_plural': 'meal plans',
            },
        ),
    ]
