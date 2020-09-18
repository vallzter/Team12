# Generated by Django 3.1.1 on 2020-09-18 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_auto_20200918_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
        migrations.AddField(
            model_name='cart',
            name='created',
            field=models.DateField(auto_now_add=True, default=0, verbose_name='Ceation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='web_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cart_owner', to='auth.user', verbose_name='Web User'),
            preserve_default=False,
        ),
    ]
