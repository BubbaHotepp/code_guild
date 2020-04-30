from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    created_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    text = models.CharField(max_length=500)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def completed(self):
        self.completed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.task