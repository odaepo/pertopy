from django.urls import path
from .views import task_list, create_task, TaskListView, TaskUpdateView

urlpatterns = [
    path('tasklist', TaskListView.as_view(), name='task_listauto'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks', task_list, name='task_list'),
    path('createtask', create_task, name='create_task'),
    path('uupdateTask/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
]
