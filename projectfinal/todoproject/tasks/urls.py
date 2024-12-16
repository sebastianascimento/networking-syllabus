from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    
    path('api/tasks/', views.TaskList.as_view(), name='task_list'),
    path('api/tasks/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),

    
    path('', views.task_list, name='task_list'),  
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
