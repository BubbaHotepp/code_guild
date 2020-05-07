from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('shortenapp/<pk>/url_encode', views.url_encode, name='url_encode'),
]