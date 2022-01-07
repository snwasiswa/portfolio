from django import forms
from django.db.models import fields
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form for the contact"""

    name = forms.CharField(max_length=120, required=True, widget=forms.TextInput(
        attrs={'placeholder':'Full name','class':'form-control'}))
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'placeholder':'Email','class':'form-control'}))
    phone = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={'placeholder':'Phone number','class':'form-control'}))
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(
        attrs={'placeholder':'Your message','rows': 7,'class':'form-control'}))

    class Meta:
        model = Contact
        fields = ('name','email','message',)