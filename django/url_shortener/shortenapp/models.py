from django.conf import settings
from django.db import models
from django.utils import timezone

class Shorten(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    created_date = models.DateField(default=timezone.now)
    visits = models.IntegerField(default=0)

    def clicks(self):
        self.visits += 1
        self.save()