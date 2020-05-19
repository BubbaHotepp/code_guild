from django.urls import path
from . import views

urlpatterns = [
        path('', views.home_page, name='home_page'),
        path('book_list', views.book_list, name='book_list'),
        path('author_list', views.author_list, name='author_list'),
        path('book_details', views.book_details, name='book_details'),
        path('author_info', views.author_info, name='author_info'),
        path('catalog_search', views.catalog_search, name='catalog_search'),
        path('books/', views.BookListView.as_view(), name='books'),
        path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]