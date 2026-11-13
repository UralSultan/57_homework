from django import forms
from task_man.models import Project

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['start_date', 'end_date', 'title', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }