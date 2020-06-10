from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/registration.html', {'form':form})