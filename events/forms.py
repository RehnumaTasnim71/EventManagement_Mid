from django import forms
from .models import Event, Category

class EventForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'input'}),
        required=False, 
        empty_label="Select a category"
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'image', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Event Title'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Event Description'}),
            'category': forms.Select(attrs={'class': 'input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input'}),
            'date': forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'}),
        }
