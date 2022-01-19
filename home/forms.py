from django import forms
from django.db.models import fields
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import HttpResponse
from django.conf import settings


class ContactForm(forms.ModelForm):
    """Form for the contact"""

    name = forms.CharField(max_length=120, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Full name', 'class': 'form-control'}))
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={'placeholder': 'Phone number', 'class': 'form-control'}))
    subject = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Your message', 'rows': 7, 'class': 'form-control'}))

    def get_message(self):

        clean_data = super().clean()

        name = clean_data.get('name')
        email = clean_data.get('email')
        phone = clean_data.get('phone')
        subject = clean_data.get('subject')
        message_to_send = clean_data.get('message')

        message = f'You got a new message:\n\n'
        message += f'Sender Info:\n'
        message += f'\n"Subject : {subject}"'
        message += f'\n"Name : {name}"'
        message += f'\n"Email : {email}"'
        message += f'\n"Phone number : {phone}"\n\n'
        message += f'\n{message_to_send}\n\n'

        return message, subject

    def send_email(self):

        message, subject = self.get_message()

        try:
            send_mail(subject, message, from_email=str(settings.ADMIN_EMAIL),
                      recipient_list=[str(settings.ADMIN_EMAIL)], fail_silently=False, )
        except BadHeaderError:
            return HttpResponse('Invalid header found')

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message',)
