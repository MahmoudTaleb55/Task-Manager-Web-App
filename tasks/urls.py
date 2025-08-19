from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('toggle/<int:pk>/', views.task_toggle_status, name='task_toggle_status'),
    path('delete_all/', views.delete_all_tasks, name='delete_all_tasks'),
]