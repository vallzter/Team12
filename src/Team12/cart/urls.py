from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/', views.add, name='add_item')
]