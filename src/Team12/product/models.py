from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _

class MealPlan(models.Model):
<<<<<<< HEAD
    
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    recipe = models.TextField(blank=False)
=======

    name        = models.CharField(max_length=50)
    price       = models.IntegerField()
    recipe      = models.TextField(blank=False)
>>>>>>> master
    ingredients = models.TextField(blank=False, default="N/A")
    image       = models.CharField(max_length=255)

    objects     = models.Manager()

    class Meta:
        verbose_name = _("meal plan")
        verbose_name_plural = _("meal plans")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MealplanDetailed", kwargs={"pk": self.pk})
        # return reverse_lazy('MealplanDetailed', kwargs={'pk': self.pk}, current_app='products')
