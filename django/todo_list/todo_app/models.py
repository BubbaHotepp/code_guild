from django.conf import settings
from django.db import models
from django.db.models import Model
from django.utils import timezone
from django import forms

class Taskpost(Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=150)
    detail_text = models.TextField()
    posted_date = models.DateField(default=timezone.now)
    is_complete = models.BooleanField()
    completed_date = models.DateField(blank=True, null=True)

    def completed(self):
        self.completed_date = timezone.now()
        self.save

    def finished(self):
        self.is_complete = True

    def __str__(self):
        return self.task

    