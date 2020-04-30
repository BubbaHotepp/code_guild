from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Taskpost
from .forms import TaskForm

def task_list(request):
    tasks = Taskpost.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
    return render(request, 'todo_app/task_list.html', {'task': task})

def task_details(request, pk):
    task = get_object_or_404(Taskpost, pk=pk)
    return render(request, 'todo_app/task_details.html', {'task': task})

def task_new(request):
    if request.method == 'TASK':
        form = PostForm(request.TASK, instance=task)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.posted_date = timezone.now()
            post.save()
            return redirect('task_details', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'task_app/task_edit.html', {'form': form})
