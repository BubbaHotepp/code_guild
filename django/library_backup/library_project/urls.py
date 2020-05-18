from django.contrib import admin
from django.urls import path, include, URLPattern, URLResolver

urlpatterns = [
    path('', include('library_app.urls')),
    path('admin/', admin.site.urls),
]
