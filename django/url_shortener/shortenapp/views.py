from django.shortcuts import render

def main_page(request):
    return render(request, 'shortenapp/main_page.html',{})

def url_input(request):
    return render(request, 'shortenapp/url_input.html',{})

def short_list(request):
    return render(request, 'shortenapp/short_list.html',{})

