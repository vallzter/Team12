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
    User page
    '''
    return render(request, 'user/user_page.html')


@login_required
def profile(request):
    return render(request, 'user/profile.html')


def remove_user(request):
    user = request.user
    if user.is_authenticated:
        if not user.is_superuser:
            request.user.delete()
            return HttpResponse(f'{user.username} was deleted')
    
    return HttpResponse('Must be logged in to delete user')