from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import timezone
from datetime import datetime

class ShippingAddress(models.Model):

    country = models.CharField(_("Country"), max_length=50)
    region  = models.CharField(_("Region/State"), max_length=50)
    city    = models.IntegerField(_("Postcode"))
    street  = models.CharField(_("Street address"), max_length=50)
    info    = models.CharField(_("Additional info"), max_length=50)

    class Meta:
        verbose_name = _("shippingaddress")
        verbose_name_plural = _("shippingaddress'")

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

    def get_absolute_url(self):
        return reverse("shippingaddress_detail", kwargs={"pk": self.pk})


class PaymentMethod(models.Model):

    cardnumber = models.CharField(_("Card number"), max_length=16)                   # TODO: Implement encryption
    CVV        = models.CharField(_("Card Verification Value"), max_length=4)        # TODO: Implement encryption
    date       = models.DateField(_("Expiration date"), auto_now=False, auto_now_add=False)
    name       = models.CharField(_("Cardholder name"), max_length=50)

    class Meta:
        verbose_name = _("PaymentMethod")
        verbose_name_plural = _("PaymentMethods")

    def __str__(self):
        return f"Card: XXXX-XXXX-XXXX-{self.cardnumber[-4:]}"

    def get_absolute_url(self):
        return reverse("PaymentMethod_detail", kwargs={"pk": self.pk})


class LineItem(models.Model):

    quantity = models.IntegerField(_("Quantity"))
    mealplan = models.ForeignKey("product.MealPlan", verbose_name=_(""), on_delete=models.CASCADE)
    cart     = models.ForeignKey("Cart", verbose_name=_("Cart"), on_delete=models.CASCADE)

    def get_price(self):
        return self.mealplan.price * self.quantity

    class Meta:
        verbose_name = _("lineitem")
        verbose_name_plural = _("lineitems")

    def __str__(self):
        return f"Cart#{self.id}"

    def get_absolute_url(self):
        return reverse("lineitem_detail", kwargs={"pk": self.pk})


class Cart(models.Model):

    customer = models.ForeignKey("user.Customer", verbose_name=_("Customer"), on_delete=models.PROTECT)
    web_user = models.ForeignKey(get_user_model(), verbose_name="Web User", on_delete=models.CASCADE, related_name="cart_owner")
    created  = models.DateField(_("Ceation date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"Cart#{self.id}"

    def get_absolute_url(self):
        return reverse("Cart_detail", kwargs={"pk": self.pk})

    @classmethod
    def create(cls, user):
        return cls(web_user=user, created=timezone.now())


class Order(models.Model):

    customer = models.ForeignKey("user.Customer", verbose_name=_("Customer"), on_delete=models.PROTECT)
    ordered  = models.DateField(_("Order date"), auto_now=False, auto_now_add=True)
    shipped  = models.DateField(_("Shipping date"), auto_now=False, auto_now_add=False)
    ship_to  = models.OneToOneField("ShippingAddress", verbose_name=_("Ship To"), on_delete=models.CASCADE)
    status   = models.CharField(_("Status"), max_length=20)
    total    = models.IntegerField(_("Total"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order#{self.id}"

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
