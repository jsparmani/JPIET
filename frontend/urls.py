from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('home-image/', views.home_image, name='home_image'),
]
