from django.db.models.functions import datetime
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Cart
import logging

# Create your views here.
def add_to_cart(request, **kwargs):
    user = request.user.username
    if Cart.objects.filter(web_user=user):
        if request.method == "POST":
            cart = Cart(request.user, created=datetime.now())
            logging("added")