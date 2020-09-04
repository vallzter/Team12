from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, 'user/register.html')