from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task category'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Select due date', 'type': 'datetime-local'}),
        }

class TaskSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search tasks...',
            'aria-label': 'Search tasks'
        })
    )
    
    category = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filter by category...'
        })
    )
    
    priority = forms.ChoiceField(
        required=False,
        choices=[('', 'All Priorities')] + Task._meta.get_field('priority').choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'All Statuses'), ('completed', 'Completed'), ('pending', 'Pending')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
