from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index , name='Index'),
    path("register/", views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('profile/', views.profile, name='profile'),
    path('remove/', views.remove_user, name='remove'),
    path('edit/', views.editProfileRedirect, name='editProfileRedirect'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('cancel/', views.cancelSubscription, name='cancel')
]
