from django.db import models
from django.urls import reverse, reverse_lazy


class MealPlan(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    recipe = models.TextField(blank=False)
    ingredients = models.TextField(blank=False, default="N/A")
    image = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name = "meal plan"
        verbose_name_plural = "meal plans"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MealplanDetailed", kwargs={"pk": self.pk})
        # return reverse_lazy('MealplanDetailed', kwargs={'pk': self.pk}, current_app='products')
