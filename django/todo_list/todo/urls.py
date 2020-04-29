from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('', views.task_input, name='task_input'),
]