from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random, string
from django.conf import settings
from .models import Shorten

def main_page(request):
    return render(request, 'shortenapp/main_page.html')

def short_list(request):
    short_list = {}
    short_list.update(request)
    return render(request, 'shortenapp/short_list.html')

def redirect_original(request, short_url):
    url = get_object_or_404(Shorten, pk=short_url)
    url.visits += 1
    url.save()
    return redirect(url.original_url)

def url_short(request):
    if not (url == ''):
        short_url = url_encode()
        shorty = Shorten(original_url=url, short_url=short_url)
        shorty.save()
        short_db = {}
        short_db['url'] = settings.SITE_URL + '/' + short_url
        return redirect('main_page.html')
    return render(request, 'shortenapp/main_page.html')

def url_encode():
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits
    length = 8
    x = 0
    while x <= 8:
        url_short = ''.join(random.choice(char))
        x += 1
    return url_short

