from django.urls import path
from .views import task_list, create_task

urlpatterns = [
    path('tasks', task_list, name='task_list'),
    path('createtask', create_task, name='create_task'),
]
