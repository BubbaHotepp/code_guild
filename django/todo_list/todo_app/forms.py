from django import forms
from .models import Taskpost

class TaskForm(forms.ModelForm):
    class Meta:
        model = Taskpost
        fields = ('task', 'detail_text',)