# todoproject/urls.py
from django.contrib import admin
from django.urls import path , include
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'tasks/task_list.html')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
]
