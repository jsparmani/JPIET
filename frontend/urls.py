from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('change-home-image/', views.change_home_image, name='change_home_image'),
    path('change-stats/', views.change_stats, name='change_stats'),
    path('add-notice/', views.add_notice, name='add_notice'),
    path('view-notices/', views.view_notices, name='view_notices'),
    path('delete-notice/<int:pk>/', views.delete_notice, name='delete_notice'),
    path('edit-notice/<int:pk>/', views.edit_notice, name='edit_notice'),
    path('add-media/', views.add_media, name='add_media'),
    path('view-medias/', views.view_medias, name='view_medias'),
    path('delete-media/<int:pk>/', views.delete_media, name='delete_media'),
    path('add-event/', views.add_event, name='add_event'),
    path('view-events/', views.view_events, name='view_events'),
    path('delete-event/<int:pk>/', views.delete_event, name='delete_event'),
    path('edit-event/<int:pk>/', views.edit_event, name='edit_event'),
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),
    path('view-testimonials/', views.view_testimonials, name='view_testimonials'),
    path('delete-testimonial/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
    path('edit-testimonial/<int:pk>/', views.edit_testimonial, name='edit_testimonial'),
    path('add-recruiter/', views.add_recruiter, name='add_recruiter'),
    path('view-recruiters/', views.view_recruiters, name='view_recruiters'),
    path('delete-recruiter/<int:pk>/', views.delete_recruiter, name='delete_recruiter'),
    path('get-about-us/', views.get_about_us, name='get_about_us'),
    path('change-message/<int:uid>/', views.change_message, name='change_message'),
    path('view-about-us/<int:uid>/', views.view_about_us, name='view_about_us'),
    path('add-infrastructure/', views.add_infrastructure, name='add_infrastructure'),
    path('edit-infrastructure/<int:pk>/', views.edit_infrastructure, name='edit_infrastructure'),
    path('delete-infrastructure/<int:pk>/', views.delete_infrastructure, name='delete_infrastructure'),
    path('change-vision-mission/', views.change_vision_mission, name='change_vision_mission'),
]
