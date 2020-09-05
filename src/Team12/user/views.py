from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
        else:
            messages.error(request, 'Registration failed!')
            messages.error(request, form.errors)
        
    form = UserCreationForm()
    args = {"form": form}
    return render(request, "user/register.html", args)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return None

@login_required
def profile(request):
    return render(request, 'user/profile.html')
