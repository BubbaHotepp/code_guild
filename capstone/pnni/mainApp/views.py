from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from accounts.models import User_flag


def home(request):
    return render(request, 'home.html')

def forum(request):
    return render(request, 'forum/')

def inbox(request):
    return render(request, 'messages/inbox')

def staff_page(request):
    user=request.user.id
    id_check = User_flag.objects.get(id=user).user_type
    if id_check == 'Staff':
        return render(request, 'admin/staff-page.html')
    else:
        return render(request, 'home.html')
