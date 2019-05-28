
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static



urlpatterns = [
    
    # path('', views.email_check, name='email_check'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)