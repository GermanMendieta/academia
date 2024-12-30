from django.urls import path
from . import views

app_name = 'alumnos'

urlpatterns = [
    path('', views.alumnos_view, name='alumnos_view'),
    path('edit/<int:id>/', views.edit_alumno, name='edit_alumno'),
    path('delete/<int:id>/', views.delete_alumno, name='delete_alumno'),
    path('multiple_selected/', views.selected_multiple_alumnos, name='multiple_selected'),
    path('add_responsable/', views.add_responsable, name='add_responsable'),
    path('edit_responsable/<int:id>/', views.edit_responsable, name='edit_responsable'),
    path('delete_responsable/<int:id>/', views.delete_responsable, name='delete_responsable'),
    path('associate_responsables/', views.associate_responsables, name='associate_responsables'),
]
