from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

class Customer(models.Model):

    web_user   = models.ForeignKey(get_user_model(), verbose_name="Web User", on_delete=models.CASCADE, related_name="webuser")
    address    = models.OneToOneField("cart.ShippingAddress", verbose_name="Shipping Address", on_delete=models.CASCADE)
    payment    = models.OneToOneField("cart.PaymentMethod", verbose_name="Payment Method", on_delete=models.CASCADE)
    first_name = models.CharField("First name", max_length=50)
    last_name  = models.CharField("Last name", max_length=50)
    email      = models.EmailField("Email", max_length=254)
    phone      = models.IntegerField("Phone")

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})
