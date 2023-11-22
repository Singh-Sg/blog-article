# yourappname/forms.py
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea)
