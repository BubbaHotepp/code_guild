from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_list, name='item_list')
]