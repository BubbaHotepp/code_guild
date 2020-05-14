from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Task(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    task_title = models.CharField(max_length=100)
    task_text = models.TextField()
    posted_date = models.DateField(default=timezone.now)
    checkbox = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def complete_check(self):
        if self.checkbox == True:
            self.completed_date = timezone.now()
            self.save()
        else:
            pass
    
    def __str__(self):
        return self.task_title