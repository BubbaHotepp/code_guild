from django.contrib import admin
from .models import Category, Book, Document, Author, Record, Photograph

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Document)
admin.site.register(Author)
admin.site.register(Record)
admin.site.register(Photograph)
