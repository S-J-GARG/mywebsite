from django import forms
from .models import ContactForm
# Code for contact us form
class ContactUsform(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['Name', 'Email', 'Message']
