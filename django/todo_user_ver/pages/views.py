from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html', {'index': index})

def about(request):
    return render(request, 'pages/about.html', {'about': about})