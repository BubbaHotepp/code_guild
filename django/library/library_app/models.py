from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

class Category(models.Model):
    name = models.CharField(max_length=200)    

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-details', args[str(self.id)])

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
    catalog_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    checkout_date = models.DateField(null=True, default=timezone.now)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

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

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f'{self.id} ({self.book.title})'