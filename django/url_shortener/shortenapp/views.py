from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random, string
from django.conf import settings
from .models import Shorten

def main_page(request):
    return render(request, 'shortenapp/main_page.html')

def url_short(request):
    short_url = url_encode()
    url = request.POST.get('url')
    shorty = Shorten(original_url=url, short_url=short_url)
    shorty.save()
    short_db = {}
    short_db['url'] = settings.SITE_URL + '/' + short_url
    return redirect('main_page')

def url_encode():
    length = 8
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits
    short_url = ""
    x = 0
    while x <= 8:
        short_url += random.choice(char)
        x += 1
    return short_url

def redirect_original(request, short_url):
    url = get_object_or_404(Shorten, pk=short_url)
    url.visits += 1
    url.save()
    return redirect(url.original_url)

def short_list(request, short_url):
    url = get_object_or_404(Shorten, pk=short_url)

    
