from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('staff_page', views.staff_page, name='staff_page'),
    path('inbox', views.inbox, name='inbox'),
    path('outbox', views.outbox, name='outbox'),
    path('compose', views.compose, name='compose'),
    path('trash', views.compose, name='trash'),
    path('view_message', views.compose, name='view_message'),
    path('new_message', views.compose, name='new_message'),
]
