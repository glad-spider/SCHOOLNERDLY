from .models import Task
from django.forms import ModelForm, TextInput, Textarea

# class - == form
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"] # название полей в форме
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите описание'
            }),
        }
