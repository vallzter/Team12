from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
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
    print("im here")
    if request.method == "GET":
        raise Http404()
    prod_id = request.POST.get('id')
    print(prod_id)
    print("im here")
    quantity = request.POST.get('quantity') or 1
    prod = MealPlan.objects.get(pk=prod_id)
    customer = request.user.customer
    user_cart = Cart.objects.get(web_user=user)
    if user_cart:
        cart_item = LineItem(quantity=quantity,product=prod,cart=user_cart)
        cart_item.save()
    else: # create one
        new_cart = Cart(user=request.user,
                        status='Active')
        new_cart.save()
        cart_item = LineItem(quantity=quantity,
                              product=prod,
                              cart=new_cart)
        cart_item.save()
    messages.info(request, f"{prod.name} has been added to your cart.")
    return render(request, 'cart/index.html')

        