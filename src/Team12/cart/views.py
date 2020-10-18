from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
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
    customer = User.objects.get(username=request.user)
    try:
        cart = Cart.objects.get(web_user=customer)
        cart_items = LineItem.objects.filter(cart=cart) if cart else None
    except:
        cart = None
        cart_items = None
        
    context = {
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'cart/index.html', context=context)
    
@login_required
def add(request): 
    # add item to cart
    if request.method != "POST":
        raise Http404()
    prod_id = request.POST.get('id')
    quantity = request.POST.get('quantity') or 1
    prod = MealPlan.objects.get(pk=prod_id)
    customer = User.objects.get(username=request.user)
    user_cart, create = Cart.objects.get_or_create(web_user=customer)
    
    if user_cart.contains(prod):#add to quantity
        all_items = LineItem.objects.filter(cart=user_cart)
        meal = all_items.get(mealplan=prod)
        meal.quantity += int(quantity)
        meal.save()
    else:
        cart_item = LineItem(quantity=quantity,mealplan=prod,cart=user_cart)
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) # Redirects back after post method

@login_required
def edit_quantity(request):
    if request.method != "POST":
        raise Http404()
    customer = User.objects.get(username=request.user)
    prod_id = request.POST.get('id')
    quantity = request.POST.get('quantity') or 1
    user_cart = 0
    try:
        user_cart = Cart.objects.get(web_user=customer)
    except:
        pass
    if user_cart:
        prod = MealPlan.objects.get(pk=prod_id)
        all_items = LineItem.objects.filter(cart=user_cart)
        meal = all_items.filter(mealplan=prod).get(mealplan=prod)
        meal.quantity = int(quantity)
        meal.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) # Redirects back after post method

@login_required
def change_quantity(request):
    if request.method != "POST":
        raise Http404()
    customer = User.objects.get(username=request.user)
    mealplan = request.POST.get('id')
    quantity = request.POST.get('quantity')
    cart, create_cart = Cart.objects.get_or_create(web_user=customer)
    item, create_item = LineItem.objects.get_or_create(cart=cart, mealplan=mealplan)
    
    item.quantity = quantity
    item.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) # Redirects back after post method

@login_required
def subscribe(request):
    if request.method != "POST":
        raise Http404()
    user = User.objects.get(username=request.user)
    prod_id = request.POST.get('id')
    prod = MealPlan.objects.get(pk=prod_id)
    customer = Customer.objects.get(web_user=user)
    customer.subscription = prod#adds priduct id to subscription
    customer.save()
    return redirect(index)


@login_required
def delete(request):
    if request.method != "POST":
        raise Http404()
    customer = User.objects.get(username=request.user)
    prod_id = request.POST.get('id')
    user_cart = 0
    try:
        user_cart = Cart.objects.get(web_user=customer)
    except:
        pass
    if user_cart:
        # delete item from cart
        prod = MealPlan.objects.get(pk=prod_id)
        all_items = LineItem.objects.filter(cart=user_cart)
        meal = all_items.filter(mealplan=prod).get(mealplan=prod)
        meal.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) # Redirects back after post method

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
        