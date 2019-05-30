
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static



urlpatterns = [
    
    # path('', views.email_check, name='email_check'),
    
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('fault/<str:fault>', views.fault, name='fault'),
    path('success/<str:success>', views.success, name='success'),
    path('account/', include('account.urls', namespace='account')),
    path('frontend/', include('frontend.urls', namespace='frontend')),
    path('faculty/', include('faculty.urls', namespace='faculty')),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)