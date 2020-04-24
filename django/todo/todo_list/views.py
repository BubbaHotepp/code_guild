from django.shortcuts import render

def item_list(request):
    return render(request, 'todo_list/item_list.html')