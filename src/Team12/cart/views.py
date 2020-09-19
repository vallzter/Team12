from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import MealPlan
from user.models import Customer
from cart.models import LineItem, Cart

@login_required
def index(request):
    #todo, send context to cart/index.html
    return render(request, 'cart/index.html')

# Create your views here.
def add(request):
    # add item to cart
    if request.method == "GET":
        pass #todo, add item to cart