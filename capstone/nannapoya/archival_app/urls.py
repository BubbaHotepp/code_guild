from django.urls import path, include
from . import views

urlpatterns = [
    path('archive-home', include('archive-home.html')),
]