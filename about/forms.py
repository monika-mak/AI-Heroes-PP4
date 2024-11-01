from .models import CommunicationRequest
from django import forms

class CommunicationForm(forms.ModelForm):
    class Meta:
        model = CommunicationRequest
        fields = ('name', 'email', 'message')


