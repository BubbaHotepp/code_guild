from django.contrib import admin
from .models import Category, Author, Books, Book_loan

admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Book_loan)