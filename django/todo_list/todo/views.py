from django.shortcuts import render
from django.utils import timezone
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo/task_list.html', {})

def task_input(request):
    return render(request, 'todo/task_input.html', {})
    
