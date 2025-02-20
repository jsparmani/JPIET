from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
    path('signup/',views.signup, name = 'signup'),
    path('user-list/',views.user_list, name = 'user_list'),
    path('delete-user/<int:pk>/',views.delete_user, name = 'delete_user'),
]
