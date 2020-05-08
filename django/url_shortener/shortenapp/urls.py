from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('', views.short_list, name='short_list'),
    path('url_short', views.url_short, name='url_short'),
]