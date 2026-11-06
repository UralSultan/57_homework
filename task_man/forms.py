from django import forms
from django.forms import widgets
from .models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='Загаловок')
    description = forms.CharField(max_length=1000, required=True, widget=widgets.Textarea(attrs={'rows': 4}),
                                  label='Описание')
    status = forms.ModelChoiceField(required=True, queryset=Status.objects.all(),
                                    label='Статус')
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Типы')