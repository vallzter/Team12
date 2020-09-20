from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from product.models import MealPlan
from django.contrib.auth.models import User
from django.utils import timezone
from cart.models import LineItem, Cart

@login_required
def index(request):
    #todo, send context to cart/index.html
    try:
        customer = User.objects.get(username=request.user)
        cart = Cart.objects.get(web_user=customer)
        cart_items = LineItem.objects.filter(cart=cart) if cart else None
        context = {
            'cart': cart,
            'cart_items': cart_items
        }
        return render(request, 'cart/index.html', context=context)
    except:
        return render(request, 'cart/index.html')

def add(request):
    # add item to cart
    if request.method == "GET":
        raise Http404()
    prod_id = request.POST.get('id')
    quantity = request.POST.get('quantity') or 1
    prod = MealPlan.objects.get(pk=prod_id)
    customer = User.objects.get(username=request.user)
    user_cart = 0
    try:
        user_cart = Cart.objects.get(web_user=customer)
    except:
        pass
    if user_cart:
        if user_cart.contains(prod):
            all_items = LineItem.objects.filter(cart=user_cart)
            meal = all_items.filter(mealplan=prod).get(mealplan=prod)
            meal.quantity += int(quantity)
            meal.save()
        else:
            cart_item = LineItem(quantity=quantity,mealplan=prod,cart=user_cart)
            cart_item.save()
    else:
        new_cart = Cart(web_user=customer, created=timezone.now())
        new_cart.save()
        cart_item = LineItem(quantity=quantity,mealplan=prod,cart=new_cart)
        cart_item.save()
    return redirect(index)

def checkout(request):
    return render(request, 'cart/checkout.html')
        