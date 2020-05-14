from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/checkbox/<int:pk>/', views.checkbox, name='checkbox'),
    path('task/<pk>/delete/', views.task_delete, name='task_delete'),
    path('accounts/<int:id>', views.update, name = 'accounts')
]
