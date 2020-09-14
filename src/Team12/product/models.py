from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    category = models.CharField(max_length=255)