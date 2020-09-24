from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import MealPlan

def index(request):
    data = MealPlan.objects.all() # simple index which draws all meal plans from the database

    context = {
        "products": data,
    }

    return render(request, 'products/index.html', context)

def detailed_product(request, pk): # A detailed product is genereated by primary key id
    meal_plan = get_object_or_404(MealPlan, pk=pk)

    context  = {
        "mealplan": meal_plan,
    }

    return render(request, 'products/mealplan_detailed.html', context)


def product_order(request, order):
    data = MealPlan.objects.order_by(order).all() # Here the product gets ordered in accending or descending order dependingon the def input var

    context = {
        "products": data,
    }

    return render(request, 'products/index.html', context)

def filter_price(request, filter, filter2):
    data = MealPlan.objects.filter(price__gte = filter, price__lte = filter2) # The mealplan get filtered by two parameters (Greater less and equal)

    context = {
        "products": data,
    }

    return render(request, 'products/index.html', context)