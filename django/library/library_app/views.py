from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Category, Book, Book_copies, Author, Catalog_record, User_flag
from django.views import generic
from django.db import models
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page

def home_page(request):
    book_count = Book.objects.all().count()
    total_copies_count = Book_copies.objects.all().count()
    available_book_count = Book_copies.objects.filter(status='a').count()
    author_count = Author.objects.all().count()

    context = {
        'book_count' : book_count,
        'total_copies_count' : total_copies_count,
        'available_book_count' : available_book_count,
        'author_count' : author_count,
    }
    return render(request, 'library_app/home.html', context)

def book_list(request):
    all_books = Book.objects.all()
    context = {'all_books':all_books}
    return render(request, 'library_app/book_list.html', context)

def author_list(request):
    all_authors = Author.objects.all()
    context = {'all_authors':all_authors}
    return render(request, 'library_app/author_list.html', context)

def author_info(request, id):
    author_info = Author.objects.get(id=id)
    authors_books = Book.objects.filter(author=id)
    context = {'author_info':author_info, 'authors_books':authors_books}
    return render(request, 'library_app/author_info_page.html', context)

def book_details(request, id):
    book_info = Book.objects.get(id=id)
    context = {'book_info':book_info}
    return render(request, 'library_app/book_details_page.html', context)

def checkout_book(request, id):
    checkout = Book_copies.object.get(id=id)
    user = request.user
    checkout.due_date = timezone.now() + timedelta(weeks=2)
    checkout.checkout_date = timezone.now()
    checkout.status = 'o'
    record = Catalog_record.catalog_id
    return render(request, 'library_app/home.html')

def checkin_book(request, id):
    book = Book_copies.object.get(id=id)
    book.status = 'a'
    return render(request, 'library_app/home.html')

@cache_page(60 * 15)
@csrf_protect
def catalog_search(request):
    if request.method == 'POST':
        book_name = request.POST.get('user_input')
        print(request)
        print(book_name)
        if book_name != None:
            result = Book.objects.filter(title__icontains=book_name)
            context = {'result':result}
            return render(request, 'library_app/catalog_search.html', context)
        else:
            return render(request, 'library_app/catalog_search.html')
    else:
        return render(request, 'library_app/catalog_search.html')

def catalog_status(request):
    user=request.user.id
    id_check = User_flag.objects.get(id=user).user_type
    if id_check == 'Staff':
        return render(request, 'staff_pages/catalog_status.html')
    else:
        return render(request, 'library_app/home.html')

def staff_page(request):
    user=request.user.id
    id_check = User_flag.objects.get(id=user).user_type
    if id_check == 'Staff':
        return render(request, 'staff_pages/staff_page.html')
    else:
        return render(request, 'library_app/home.html')

def books_checked_out(request, id):
    books_out = Book_copies.objects.filter(user=id)
    context = {'books_out':books_out}
    return render(request, 'library_app/home.html', context)

def book_copy_status(request, id):
    book_copy = Book_copies.objects.get(id=id)
    context = {'status':status}
    return render(request, 'library_app/book_list.html', context)

def reserve_book(request, id):
    book_copy = Book_copies.objects.get(id=id)
    status = book_copy.status
    status = 'Reserved'
    context = {'status':status}
    return render(request, 'library_app/book_list.html', context)