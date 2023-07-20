from django.urls import path
from teamwork.tasks.views import (
    TasksApiView, 
    TasksRApiView,
    TasksCreateApiView,
    TasksDeleteApiView,
    TasksUpdateApiView
    ) 
app_name = "tasks"
urlpatterns = [
    path('', TasksApiView.as_view(), name='tasks'),
    path('task_detail/<int:pk>/', TasksRApiView.as_view(), name='detail'),
    path('task_delete/<int:pk>/', TasksDeleteApiView.as_view(), name='delete'),
    path('task_update/<int:pk>/', TasksUpdateApiView.as_view(), name='update'),
    path('task_create/', TasksCreateApiView.as_view(), name='create'),
]

