from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
User = get_user_model()

def register(request):
    if request.method == 'POST':
        new_user = User(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        return redirect('login')    
    else:
        return render(request, 'user_accounts/register.html', {'register': register})

def login_user(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user is not None:
            login_user(request, user)
            return redirect('home')
        else:
            pass
    else:
        return render(request, 'user_accounts/login.html', {'login_user': login_user})

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')
