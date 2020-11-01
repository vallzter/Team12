from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/', views.add, name='add_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('delete/', views.delete, name="delete"),
    path('edit_quantity/', views.edit_quantity, name="edit_quantity"),
    path('edit_size/', views.edit_size, name="edit_size"),
    path('change_quantity/', views.change_quantity, name="change_quantity"),
    path('subscribe/', views.subscribe, name="subscribe")
]