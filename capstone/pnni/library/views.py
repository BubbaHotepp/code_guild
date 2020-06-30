from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Category, Book, Document, Author, Record, Photograph
from django.views import generic
from django.db import models
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page

def archive_page(request):
    book_count = Book.objects.all().count()
    document_count = Document.objects.all().count()
    record_count = Record.objects.all().count()
    photo_count = Photograph.objects.all().count()

    context = {
        'book_count' : book_count,

        'document_count' : document_count,

        'record_count' : record_count,

        'photo_count' : photo_count,
    }
    return render(request, 'library/archive-main.html', context)

def book_list(request):
    all_books = Book.objects.all()
    context = {'all_books':all_books}
    return render(request, 'library/book-list.html', context)

def document_list(request):
    all_documents = Document.objects.all()
    context = {'all_documents':all_documents}
    return render(request, 'library/document-list.html', context)

def record_list(request):
    all_records = Record.objects.all()
    context = {'all_records':all_records}
    return render(request, 'library/record-list.html', context)

def photo_list(request):
    all_photos = Photograph.objects.all()
    context = {'all_photos':all_photos}
    return render(request, 'library/photo-list.html', context)

def author_list(request):
    all_authors = Author.objects.all()
    context = {'all_authors':all_authors}
    return render(request, 'library/author-list.html', context)

def author_info(request, id):
    author_info = Author.objects.get(id=id)
    authors_books = Book.objects.filter(author=id)
    authors_documents = Document.objects.filter(author=id)
    context = {'author_info':author_info, 'authors_books':authors_books, 'authors_documents':authors_documents}
    return render(request, 'library/author-info-page.html', context)

def book_details(request, id):
    book_info = Book.objects.get(id=id)
    context = {'book_info':book_info}
    return render(request, 'library/book-details-page.html', context)

def document_details(request, id):
    document_info = Document.objects.get(id=id)
    context = {'document_info':document_info}
    return render(request, 'library/document-details.html', context)

def photograph_details(request, id):
    photo_info = Photograph.objects.get(id=id)
    context = {'photo_info':photo_info}
    return render(request, 'library/photograph-details.html', context)

@cache_page(60 * 15)
@csrf_protect
def book_search(request):
    if request.method == 'POST':
        book_name = request.POST.get('user_input')
        print(request)
        print(item_name)
        if book_name != None:
            result = Book.objects.filter(title__icontains=book_name)
            context = {'result':result}
            return render(request, 'library/book-search.html', context)
        else:
            return render(request, 'library/book-search.html')
    else:
        return render(request, 'library/book-search.html')

@cache_page(60 * 15)
@csrf_protect
def document_search(request):
    if request.method == 'POST':
        document_name = request.POST.get('user_input')
        print(request)
        print(document_name)
        if document_name != None:
            result = Document.objects.filter(title__icontains=document_name)
            context = {'result':result}
            return render(request, 'library/document-search.html', context)
        else:
            return render(request, 'library/document-search.html')
    else:
        return render(request, 'library/document-search.html')

@cache_page(60 * 15)
@csrf_protect
def record_search(request):
    if request.method == 'POST':
        record_name = request.POST.get('user_input')
        print(request)
        print(record_name)
        if book_name != None:
            result = Record.objects.filter(title__icontains=record_name)
            context = {'result':result}
            return render(request, 'library/record-search.html', context)
        else:
            return render(request, 'library/record-search.html')
    else:
        return render(request, 'library/record-search.html')

@cache_page(60 * 15)
@csrf_protect
def photo_search(request):
    if request.method == 'POST':
        photo_name = request.POST.get('user_input')
        print(request)
        print(photo_name)
        if photo_name != None:
            result = Photograph.objects.filter(title__icontains=photo_name)
            context = {'result':result}
            return render(request, 'library/photo-search.html', context)
        else:
            return render(request, 'library/photo-search.html')
    else:
        return render(request, 'library/photo-search.html')
