from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name="list"),
    path('user/', views.user, name="user"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    
]

