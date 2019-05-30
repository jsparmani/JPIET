from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
   path('add-faculty/', views.add_faculty, name='add_faculty'),
   path('view-faculties/', views.view_faculties, name='view_faculties'),
   path('delete-faculty/<int:pk>/', views.delete_faculty, name='delete_faculty'),
   path('edit-faculty/<int:pk>/', views.edit_faculty, name='edit_faculty'),
]
