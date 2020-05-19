from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Category, Book, Author, Catalog_record

def home_page(request):
    book_count = Book.objects.all().count()
    total_copies_count = Catalog_record.objects.all().count()
    available_book_count = Catalog_record.objects.filter(status='a').count()
    author_count = Author.objects.count()

    context = {
        'book_count' : book_count,
        'total_copies_count' : total_copies_count,
        'available_book_count' : available_book_count,
        'author_count' : author_count,
    }

    return render(request, 'library_app/home.html', context=context)

def book_list(request):
    return render(request, 'library_app/book_list.html')

def checkout_book(request):
    pass

def checkin_book(request):
    pass

def catalog_search(request):
    pass

