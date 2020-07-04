from django.urls import path
from . import views

urlpatterns = [
        path('archive', views.archive, name='archive'),
        path('book_list', views.book_list, name='book_list'),
        path('document_list', views.document_list, name='document_list'),
        path('record_list', views.record_list, name='record_list'),
        path('photo_list', views.photo_list, name='photo_list'),
        path('author_list', views.author_list, name='author_list'),
        path('book_details/<int:id>/', views.book_details, name='book_details'),
        path('document_details/<int:id>/', views.document_details, name='document_details'),
        path('photograph_details/<int:id>/', views.photograph_details, name='photograph_details'),
        path('author_info/<int:id>/', views.author_info, name='author_info'),
        path('book_search/', views.book_search, name='book_search'),
        path('document_search/', views.document_search, name='document_search'),
        path('record_search', views.record_search, name='record_search'),
        path('photo_search', views.photo_search, name='photo_search'),
]

