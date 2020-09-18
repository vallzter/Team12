from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name='products'

urlpatterns = [
    path('', views.index , name='index'),
    path('mealplan/<int:pk>/', views.detailed_product, name='detailed'),
]
