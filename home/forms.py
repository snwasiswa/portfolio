"""
forms.py

Defines the ContactForm used on the website's contact page. It collects user information
and messages, validates input, integrates reCAPTCHA, and sends email notifications to the admin.

Includes:
- Custom form fields with Bootstrap styling.
- Phone number field with international prefix support.
- reCAPTCHA for spam protection.
- Email sending via Django's email system.
"""

from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import HttpResponse
from django.conf import settings
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.ModelForm):
    """
    A form to collect user contact data and send it to the site administrator.
    Includes email integration and reCAPTCHA validation.
    """

    name = forms.CharField(
        label="Name",
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Full name',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        label="Email",
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control'
        })
    )

    phone = PhoneNumberField(
        label="Phone number",
        required=False,
        widget=PhoneNumberPrefixWidget('', attrs={
            'placeholder': 'Phone number',
            'class': 'form-control'
        })
    )

    subject = forms.CharField(
        label="Subject",
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'form-control'
        })
    )

    message = forms.CharField(
        label="Message",
        max_length=2000,
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message',
            'rows': 7,
            'class': 'form-control'
        })
    )

    captcha = ReCaptchaField(
        required=True,
        widget=ReCaptchaV2Checkbox
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')

    def get_message(self):
        """
        Constructs the message body using the cleaned form data.

        Returns:
            tuple: A tuple of (message, subject) to be sent via email.
        """
        clean_data = super().clean()
        name = clean_data.get('name')
        email = clean_data.get('email')
        phone = clean_data.get('phone')
        subject = clean_data.get('subject')
        message_to_send = clean_data.get('message')

        message = 'You got a new message:\n\n'
        message += 'Sender Info:\n'
        message += f'\nSubject: {subject}'
        message += f'\nName: {name}'
        message += f'\nEmail: {email}'
        message += f'\nPhone number: {phone}\n\n'
        message += f'{message_to_send}\n'

        return message, subject

    def send_email(self):
        """
        Sends the constructed message to the administrator via email.

        Returns:
            HttpResponse or None: Error message if header is invalid, or None if successful.
        """
        message, subject = self.get_message()

        try:
            send_mail(
                subject,
                message,
                from_email=str(settings.ADMIN_EMAIL),
                recipient_list=[str(settings.ADMIN_EMAIL)],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found')
