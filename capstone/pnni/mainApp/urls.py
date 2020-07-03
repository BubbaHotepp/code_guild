from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forum', views.forum, name='forum'),
    path('messages', views.messages, name='messages'),
]