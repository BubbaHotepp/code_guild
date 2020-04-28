from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.CharField(max_length=250)
    posted_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)

    def completed(self):
        self.completed_date = timezone.now()
        self.save
    
    def __str__(self):
        return self.item

    