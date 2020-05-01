from django.shortcuts import render
from django.utils import timezone
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')    
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

