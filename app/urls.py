from django.urls import path
from .views import TaskCreate, TaskList, TaskDetail


urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path('task/<int:pl>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create')
]
