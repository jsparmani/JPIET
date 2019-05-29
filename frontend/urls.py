from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('change-home-image/', views.change_home_image, name='change_home_image'),
    path('change-stats/', views.change_stats, name='change_stats'),
    path('add-notice/', views.add_notice, name='add_notice'),
    path('add-media/', views.add_media, name='add_media'),
    path('add-event/', views.add_event, name='add_event'),
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),
    path('add-recruiter/', views.add_recruiter, name='add_recruiter'),
]
