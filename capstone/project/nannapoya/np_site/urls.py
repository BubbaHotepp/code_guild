from django.contrib import admin
from django.urls import path, include
from accounts import views
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('mainapp.urls')),
]