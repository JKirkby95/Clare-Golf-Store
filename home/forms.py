from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    HEARD_ABOUT_CHOICES = [
        ('', 'Select an option'),
        ('search_engine', 'Search Engine'),
        ('social_media', 'Social Media'),
        ('friend', 'Friend'),
        ('advertisement', 'Advertisement'),
        ('other', 'Other'),
    ]

    heard_about_us = forms.ChoiceField(
        choices=HEARD_ABOUT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'heard_about_us']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}),
        }
