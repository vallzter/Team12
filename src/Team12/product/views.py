from django.shortcuts import render
from django.http import HttpResponse
from .models import MealPlan as meal

def index(request):
    data = meal.objects.all()

    context = {
        "products": data
    }

    return render(request, 'products/index.html', context)