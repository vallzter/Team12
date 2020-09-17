from django.db import models
from django.urls import reverse


class MealPlan(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = "meal plan"
        verbose_name_plural = "meal plans"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("meal plan_detail", kwargs={"pk": self.pk})
