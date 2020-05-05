from django.conf import settings
from django.db import models
from django.utils import timezone

class Weblink(models.Model):
    link = models.URLField()
    originalurl = models.URLField(max_length=250)
    created_date = models.DateField(default=timezone.now)
    visits = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.originalurl
    


