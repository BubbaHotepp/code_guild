from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('/templates/pages/home.html')),
]