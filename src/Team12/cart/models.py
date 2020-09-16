from django.db import models

class Cart_item(models.Model):
    user = models.ForeignKey(user, null=True, blank=True)
    product = models.ForeignKey(Product,
                                null=True,
                                on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart',
                             on_delete=models.CASCADE)

# class Contact_info(models.Model):
#    last_name = models.CharField(max_length=64)
#    first_name = models.CharField(max_length=64)
#    country = CountryField()
#    address = models.CharField(max_length=128)
#    city = models.CharField(max_length=128)
#    postcode = models.CharField(max_length=10)
# Create your models here.
