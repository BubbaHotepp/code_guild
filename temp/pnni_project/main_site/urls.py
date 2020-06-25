from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from machina import urls as machina_urls
from filebrowser.sites import site


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('mainapp.urls')),
    path('forum/', include(machina_urls)),
    path('messages/', include('postman.urls', namespace='postman')),
    path('grappelli/', include('grappelli.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
