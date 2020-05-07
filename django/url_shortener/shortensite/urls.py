from django.contrib import admin
from django.urls import path, include, URLPattern, URLResolver

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortenapp.urls')),
    path{''}
]
