from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index , name='Index'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('profile/', views.profile, name='Profile')
]