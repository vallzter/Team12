# Generated by Django 3.1.1 on 2020-09-16 04:32

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
            ],
            options={
                'verbose_name': 'meal plan',
                'verbose_name_plural': 'meal plans',
            },
        ),
    ]
