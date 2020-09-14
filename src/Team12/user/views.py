# Http modules
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Authentication
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


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
            user = authenticate(username=username, password=password)
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
    return render(request, 'user/profile.html')


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
    