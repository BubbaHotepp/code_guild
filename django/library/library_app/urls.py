from django.urls import path
from . import views

urlpatterns = [
        path('', views.home_page, name='home_page'),
        path('home', views.home_page, name='home'),
        path('book_list', views.book_list, name='book_list'),
        path('author_list', views.author_list, name='author_list'),
        path('book_details/<int:id>/', views.book_details, name='book_details'),
        path('author_info/<int:id>/', views.author_info, name='author_info'),
        path('catalog_search', views.catalog_search, name='catalog_search'),
        path('staff_page', views.staff_page, name='staff_page'),
        path('catalog_status', views.catalog_status, name='catalog_status'),
]