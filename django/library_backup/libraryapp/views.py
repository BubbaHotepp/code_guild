from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Category, Books, Author, Book_loan

def Home(request):
    