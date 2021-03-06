from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name='products'

urlpatterns = [
    path('', views.index , name='index'),
    path('filter_price/<int:filter>/<int:filter2>/', views.filter_price, name='filter_price'), # url takes in two prices 
    path('mealplan/<int:pk>/', views.detailed_product, name='detailed'), # url takes the primary key of a product
    path('product_order/<str:order>/', views.product_order , name='product_order'), # url takes in price or -price (the latter meaning descending ordering)
]


