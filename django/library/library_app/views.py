from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Category, Book, Book_copies, Author, Catalog_record, User_flag
from django.views import generic


def home_page(request):
    book_count = Book.objects.all().count()
    total_copies_count = Book_copies.objects.all().count()
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

def author_list(request):
    return render(request, 'library_app/author_list.html')

def author_info(request):
    return render(request, 'library_app/author_info_page.html')

def book_details(request):
    return render(request, 'library_app/book_details_page.html')

def checkout_book(request):
    pass

def checkin_book(request):
    pass

def catalog_search(request):
    return render(request, 'library_app/catalog_search.html')

def catalog_status(request):
    user=request.user.id 
    id_check = User_flag.objects.get(id=id).user_type
    if id_check == 'Staff':
        return render(request, 'staff_pages/catalog_status.html')
    else:
        return render(request, 'library_app/home.html')

def user_list(request):
    user=request.user.id
    id_check = User_flag.objects.get(id=id).user_type
    if id_check == 'Staff':
        return render(request, 'staff_pages/user_list.html')
    else:
        return render(request, 'library_app/home.html')

def staff_page(request):
    user=request.user.id
    id_check = User_flag.objects.get(id=user).user_type
    if id_check == 'Staff':
        return render(request, 'staff_pages/staff_page.html')
    else:
        return render(request, 'library_app/home.html')

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'library_book_list'
    
class BookDetailView(generic.DetailView):
    model = Book

class UserDetailView(generic.DetailView):
    model = get_user_model

