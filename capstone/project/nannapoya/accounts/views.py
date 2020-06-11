from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth import get_user_model

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('registration')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/registration.html', {'form':form})

def login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            pass
    else:
        return render(request, 'accounts/login.html', {'login': login})

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')