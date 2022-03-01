from dataclasses import fields
from pyexpat import model
from django import forms
from .models import TaskList

# mention class -> talk abt which model i am connecting and which field we are goona edit

class TaskForm(forms.ModelForm):
    class Meta:
        # contain two variable models and field
        model = TaskList
        fields = ["task","done"]