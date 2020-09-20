from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from product.models import MealPlan
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Customer
from cart.models import LineItem, Cart, Order

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
    if user_cart:#work with excisting cart
        if user_cart.contains(prod):#add to quantity
            all_items = LineItem.objects.filter(cart=user_cart)
            meal = all_items.filter(mealplan=prod).get(mealplan=prod)
            meal.quantity += int(quantity)
            meal.save()
        else:#add item
            cart_item = LineItem(quantity=quantity,mealplan=prod,cart=user_cart)
            cart_item.save()
    else:#make a new one
        new_cart = Cart(web_user=customer, created=timezone.now())
        new_cart.save()
        cart_item = LineItem(quantity=quantity,mealplan=prod,cart=new_cart)
        cart_item.save()
    return redirect(index)

def checkout(request):
    #time = request.GET.get('time')
    #location = request.GET.get('location')
    #customer = User.objects.get(username=request.user)
    #customerTest = Customer.objects.get(pk=1)
    #ordered = timezone.now()
    #cart = Cart.objects.get(web_user=customer)
    #total = cart.total_price
    #new_order = Order(customer=customerTest, ordered=ordered, shipped=time, ship_to=location,status="On Hold", total=total)
    #new_order.save()
    return render(request, 'cart/checkout.html')
        