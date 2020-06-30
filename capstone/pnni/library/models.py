from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date
import uuid


class Category(models.Model):
    name = models.CharField(max_length=200)    

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(null=True, blank=True)
    published_date = models.DateField()
    category = models.ManyToManyField(Category)

    def display_category(self):
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-details')

class Document(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(null=True, blank=True)
    date_created = models.DateField()
    category = models.ManyToManyField(Category)

class Record(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(null=True, blank=True)
    date_created = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)

class Photograph(models.Model):
    subject = models.CharField(max_length=100)
    taken_by = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    date_taken = models.DateField()

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-details', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

