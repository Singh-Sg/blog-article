from article.models import ContactRequest

from django import forms


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = "__all__"
