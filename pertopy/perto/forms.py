from django import forms
from .models import Task, Status

class TaskForm(forms.ModelForm):
    def __init__(self, current_status=None, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if current_status:
            next_statuses = Status.objects.filter(children=current_status)
            self.fields['status'].queryset = Status.objects.filter(pk__in=[current_status.pk, *next_statuses.values_list('pk', flat=True)])

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'min', 'max', 'attuale', 'priorita', 'impotanza', 'minuti', 'contesto', 'scadenza']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'})
        }
