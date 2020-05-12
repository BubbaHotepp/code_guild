from django.contrib import admin
from .models import Author, Category, Books, Book_status

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Book_status)
