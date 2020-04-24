from django.conf import settings
from django.db import models
from django.utils import timezone

class Item(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)

    def complete(self):
        self.completed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.task
    
    
