from django import forms
from website.models import Event, ImportantDates, Schedule, ASO
from datetime import datetime


class EventForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Event  # 사용할 모델
        fields = ['event_type','event_name', 'teacher','content']
        widgets = {
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'event_type': 'Event Type',
            'event_name': 'Event Name',
            'teacher': 'Teacher',
            'content': 'Description',
        }

class ImportantDatesForm(forms.ModelForm):
    class Meta:
        model = ImportantDates
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
