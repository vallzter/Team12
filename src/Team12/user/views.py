# Http modules
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Authentication
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from cart.models import PaymentMethod, ShippingAddress
from user.models import Customer


def register(request):
    '''
    Registers the user for a new account and logs him in.
    
    Uses built in user creation form to let the user sign
    up.
    '''
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('firstname')
            last_name = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            login(request, user)
            return redirect('/user')

        messages.error(request, 'Registration failed!')     
        messages.error(request, form.errors)

    args = {"form": form}
    return render(request, "user/register.html", args)


def index(request):
    '''
    User page / menu
    '''
    return render(request, 'user/user_page.html')


@login_required
def profile(request):
    '''
    Let's authentiacted users view their profile
    '''
    user = User.objects.get(username=request.user)
    try:
        customer = Customer.objects.get(web_user=user)
        context = {
            'customer': customer
        }
    except:
        context = {
            'customer': None
        }
    return render(request, 'user/profile.html',context=context)


@login_required
def cancelSubscription(request):
    if request.method == "GET":
        raise Http404()
    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(web_user=user)
    customer.subscription = None#cancel all subscriptions, this will be updated later to cancel individual
    customer.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def editProfileRedirect(request):
    return render(request, 'user/edit.html')

@login_required
def editProfile(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        country = request.POST.get('country')
        region = request.POST.get('region')
        city = request.POST.get('city')
        info = request.POST.get('info')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        card_no = request.POST.get('card')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')
        cardholder = request.POST.get('name')#fetch alot of data
        user = User.objects.get(username=request.user)
        payment = PaymentMethod(cardnumber=card_no, CVV=cvv, date=date, name=cardholder)
        payment.save()#payment method saved
        shipping = ShippingAddress(country=country, region=region, city=city, street=address, info=info)
        shipping.save()#shipping address saved
        customer = Customer(web_user=user, address=shipping, payment=payment, first_name=fname, last_name=lname, email=email, phone=int(phone), subscription=None)
        customer.save()#customer created
    return redirect(index)

def remove_user(request):
    '''
    Removes user if he is not superuser (admin) and 
    is logged in.
    '''
    user = request.user
    if not user.is_authenticated:
        return HttpResponse('Must be logged in to delete user')
    if user.is_superuser:
        return HttpResponse('Delete superuser from admin')
    if request.method == "POST":
        request.user.delete()
        return redirect('/user')
    return render(request, 'user/user_remove.html')
    