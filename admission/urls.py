from django.urls import path
from . import views

app_name = 'admission'

urlpatterns = [

		path('add-application/', views.add_application, name = 'add_application'),
		path('view-application/', views.view_application, name = 'view_application'),
		path('add-candidate/<int:pk>/', views.add_candidate, name = 'add_candidate'),
		path('view-candidate/<int:pk>/', views.view_candidate, name = 'view_candidate'),

]