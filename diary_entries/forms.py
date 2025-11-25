from django import forms
from .models import DiaryEntry

class QuickEntryForm(forms.ModelForm):
    """Quick entry form for dashboard"""
    class Meta:
        model = DiaryEntry
        fields = ['pain_level', 'mood', 'content']
        widgets = {
            'pain_level': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '10',
                'placeholder': 'Pain level (0-10)'
            }),
            'mood': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'How are you feeling today?'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Quick note about your day...'
            })
        }

class DetailedEntryForm(forms.ModelForm):
    """Detailed entry form for entries page"""
    class Meta:
        model = DiaryEntry
        fields = ['location', 'pain_level', 'mood', 'sleep_hours', 'triggers', 'content']
        widgets = {
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Where is the pain located?'
            }),
            'pain_level': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '10'
            }),
            'mood': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your mood'
            }),
            'sleep_hours': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '24',
                'step': '0.5',
                'placeholder': 'Hours of sleep'
            }),
            'triggers': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'What might have triggered the pain?'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Detailed description of your experience...'
            })
        }
