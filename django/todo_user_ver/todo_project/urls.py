from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('todos/', include('todo_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('pages/', include('pages.urls')),
]
