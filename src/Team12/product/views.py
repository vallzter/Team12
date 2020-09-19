from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import MealPlan

def index(request):
    data = MealPlan.objects.all()

    context = {
        "products": data,
    }

    return render(request, 'products/index.html', context)

def detailed_product(request, pk):
    meal_plan = get_object_or_404(MealPlan, pk=pk)

    context  = {
        "mealplan": meal_plan,
    }

    return render(request, 'products/mealplan_detailed.html', context)


def product_order(request, order):
    data = MealPlan.objects.order_by(order).all()

    context = {
        "products": data,
    }

    return render(request, 'products/index.html', context)