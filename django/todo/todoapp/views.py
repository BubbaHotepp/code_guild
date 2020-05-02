from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todoapp/task_detail.html', {'task':task})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.posted_date = timezone.now()
            post.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'todoapp/task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.posted_date = timezone.now()
            post.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/task_edit.html', {'form': form})
