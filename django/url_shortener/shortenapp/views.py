from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random, string
from django.conf import settings
from .models import Shorten

def main_page(request):
    return render(request, 'shortenapp/main_page.html')

def short_list(request):
    url_data = Shorten.objects.all()
    return render(request, 'shortenapp/short_list.html', {'url_data':url_data})

def url_short(request):
    shorturl = url_encode()
    url = request.POST.get('url')
    shorty = Shorten(original_url=url, short_url=shorturl)
    shorty.save()
    short_db = {}
    short_db['url'] = settings.SITE_URL + '/redirect_original/' + shorturl
    return redirect('short_list')

def url_encode():
    length = 8
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits
    shorturl = ""
    x = 0
    while x <= 8:
        shorturl += random.choice(char)
        x += 1
    return shorturl

def redirect_original(request, slug):
    url = Shorten.objects.get(short_url=slug)
    url.visits += 1
    url.save()
    return redirect(url.original_url)


    
