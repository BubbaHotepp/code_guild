from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('np_app.urls')),
    path('', include('accounts.urls')),
    path('', include('archival_app.urls')),
]
