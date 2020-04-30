from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todoapp/task_detail.html', {'task': task})