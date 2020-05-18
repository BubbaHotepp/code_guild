from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Category, Book, Author, Catalog

def Home(request):
    return render(request, 'library_app/home.html')

def Book_list(request):
    return render(request, 'library_app/book_list.html')

