from django.forms import forms
from .models import ContactForm
# Code for contact us form
class ContactUsform(forms.Form):
    class Meta:
        model = ContactForm
        fields = ['cont_name', 'cont_email', 'query']
