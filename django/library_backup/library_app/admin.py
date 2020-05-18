from django.contrib import admin
from .models import Category, Book, Author, Catalog

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Catalog)
