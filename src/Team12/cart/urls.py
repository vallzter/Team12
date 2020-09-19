from django.urls import path, include
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cart'

urlpatterns = [
    path('mealplan/<int:pk>/add_to_cart', views.add_to_cart, name="cart:Add to cart")
=======
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/', views.add, name='add_item')
>>>>>>> master
]