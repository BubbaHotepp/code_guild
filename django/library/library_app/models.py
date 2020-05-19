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
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)

    def display_category(self):
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-details', args[str(self.id)])

class Book_copies(models.Model):
    library_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    book_title = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.library_id} ({self.book_title})'

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

class Catalog_record(models.Model):
    catalog_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    checkout_date = models.DateField(null=True, default=timezone.now, blank=True)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    LOAN_STATUS = (
                   ('a', 'Available'),
                   ('o', 'Checked Out'),
                   ('r', 'Reserved'),
                  )

    status = models.CharField(
                              max_length=1,
                              choices=LOAN_STATUS,
                              blank=True,
                              default='a',        
                             )

    @property
    def overdue(self):
        if self.due_date > date.today():
            return True
        else:
            return False

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f'{self.catalog_id} ({self.book.title})'