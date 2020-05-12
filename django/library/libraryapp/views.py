from django.shortcuts import render
from .models import Author, Book_status, Books, Category

def home(request):
    book_count = Books.objects.all().count()
    book_status_count = Book_status.objects.all().count()
    available_book_count = Book.status.objects.filter(availability = 'Available').count()
    authors_count = Author.objects.count()

    context = {
        'book_count':book_count,
        'book_status_count':book_status_count,
        'available_book_count':available_book_count,
        'authors_count':authors_count,
    }

    return render(request, 'home.html', context=context)


