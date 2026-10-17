from django import forms
from .models import Registration, Event

class RegistrationForm(forms.ModelForm):
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select an Event"
    )

    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'event']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
