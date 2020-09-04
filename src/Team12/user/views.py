from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return None

@login_required
def profile(request):
    return render(request, 'user/profile.html')