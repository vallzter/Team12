from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
from django.db.models import ManyToManyField

""" We have two models ATM commenting this one out
class Meal_package(models.Model):
    name = models.CharField(max_length=32, blank=False)
    ingredients = models.TextField(blank=False, default="N/A")
    price = models.IntegerField(blank=False)
    recipe = models.TextField(blank=False)

"""