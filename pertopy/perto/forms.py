from django import forms
from .models import Task, Contesto, Status

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'min',
            'max',
            'attuale',
            'priorita',
            'impotanza',
            'minuti',
            'contesto',
            'scadenza'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'min': forms.NumberInput(attrs={'class': 'form-control'}),
            'max': forms.NumberInput(attrs={'class': 'form-control'}),
            'attuale': forms.NumberInput(attrs={'class': 'form-control'}),
            'priorita': forms.NumberInput(attrs={'class': 'form-control'}),
            'impotanza': forms.NumberInput(attrs={'class': 'form-control'}),
            'minuti': forms.NumberInput(attrs={'class': 'form-control'}),
            'contesto': forms.Select(attrs={'class': 'form-control'}),
            'scadenza': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
