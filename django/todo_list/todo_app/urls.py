from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_details, name='task_details'),
    path('task/new/', views.task_new, name='task_new'),
]