from django.contrib import admin
from short_url.models import Weblink

class UrlAdmin(admin.ModelAdmin):
    list_display = ('link','originalurl','created_date','visits','status')
    oredering = ('-created_date',)

admin.site.register(Weblink, UrlAdmin)