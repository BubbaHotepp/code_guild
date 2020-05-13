from django.shortcuts import render
from django.contrib.auth import get_user_model, login_user, logout_user, authenticate
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
        new_user.save
        return redirect('login')    
    else:
        return render(request, 'accounts/register.html')

def login(request):
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
        return render(request, 'accounts/login.html')

def logout(request):
    loqout_user(request)
    return redirect('home')