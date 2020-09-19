from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from product.models import MealPlan
from django.contrib.auth.models import User
from django.utils import timezone
from cart.models import LineItem, Cart

@login_required
def index(request):
    #todo, send context to cart/index.html
    customer = User.objects.get(username=request.user)
    cart = Cart.objects.get(web_user=customer)
    print("cart: ", cart)
    cart_items = LineItem.objects.filter(cart=cart)
    items = []
    for i in cart_items:
        items.append(i.mealplan)

    items = list(dict.fromkeys(items)) #take out duplicates, this is dumb because quantity is lost(cart_items), we need a better fix
    
    context = {
        'cart': cart,
        'cart_items': items
    }
    return render(request, 'cart/index.html', context=context)

def add(request):
    # add item to cart
    if request.method == "GET":
        raise Http404()
    prod_id = request.POST.get('id')
    quantity = request.POST.get('quantity') or 1
    prod = MealPlan.objects.get(pk=prod_id)
    customer = User.objects.get(username=request.user)
    user_cart = Cart.objects.get(web_user=customer)
    if user_cart:
        cart_item = LineItem(quantity=quantity,mealplan=prod,cart=user_cart)
        cart_item.save()
    else: # create one
        new_cart = Cart(web_user=customer, created=timezone.now())
        new_cart.save()
        cart_item = LineItem(quantity=quantity,
                                mealplan=prod,
                                cart=new_cart)
        cart_item.save()
    messages.info(request, f"{prod.name} has been added to your cart.")
    return redirect(index)

def checkout(request):
    return render(request, 'cart/checkout.html')
        