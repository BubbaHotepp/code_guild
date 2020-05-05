from django.shortcuts import render, redirect, get_object_or_404
import random, string
from short_url.models import Weblink
from django.conf import settings
from django.core.context_processors import csrf

def  enter_url(request):
    url_list = {}
    url_list.update(csrf(request))
    return ender_to_response('url_shortener/enter_url.html',url_list)

def url_redirect(request, link):
    weblink = get_object_or_404(Weblink, pk=link)
    weblink.visits += 1
    weblink.save()
    return redirect(link.originalurl)

def shortened_url(request):
    weblink = request.POST.get('weblink', '')
    if not (weblink == ''):
        link = get_url_shortener()
        short_list = Weblink(original=weblink, link=link)
        short_list.save()
        link_data = {}
        link_data['weblink'] = settings.SITE_URL + '/' + link
        

def url_shortener():
    lenght = 8
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits

    while True:
        url_short = ''.join(random.choice(char) for len in range(length))

        try:
            temp_url = Weblink.objects.get(pk=url_short)

        except:
            return url_short

