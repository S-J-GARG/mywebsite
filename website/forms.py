from django import forms
from .models import ContactForm
# Code for contact us form
class ContactUsform(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['cont_name', 'cont_email', 'query']
