from django.conf import settings
from django.db import models
from django.utils import timezone

class Shorten(models.Model):
    original_url = models.URLField(max_length=250)
    short_url = models.SlugField(max_length=8,primary_key=True)
    created_date = models.DateField(default=timezone.now)
    visits = models.IntegerField(default=0)

    def clicks(self):
        self.visits += 1
        self.save()

    def __str__(self):
        return self.original_url