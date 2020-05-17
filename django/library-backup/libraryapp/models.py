from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
import uuid


class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    bio = models.TextField()

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    book_summary = models.TextField()
    category = models.ManyToManyField(Category)

    def get_absolute_url(self):
        return reverse('books-detail', args=[str(self.id)])

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Book_status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book_status = models.BooleanField(default=False)
    checked_in = models.DateField(default=timezone.now)
    checked_out = models.DateField(default=timezone.now)
    
    AVAILABILITY = (
        ('a', 'available'),
        ('o', 'checked out'),
        ('r', 'reserverd'),
    )
    
    availability = models.CharField(max_length = 1, choices = AVAILABILITY, blank = True, default = 'a')

    def status_check(self):
        if book_status == True:
            self.availability = 'Available'
        else:
            self.availability = 'Unavailable'

    def check_out(self):
        self.checked_out = timezone.now
        self.save

    def check_in(self):
        self.checked_in = timezone.now
        self.save

    class Meta:
        ordering = ['checked_out']
    
    def __str__(self):
        return self.id



