from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff_page', views.staff_page, name='staff_page'),
]