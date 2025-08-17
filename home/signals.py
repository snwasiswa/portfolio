"""
signals.py

Defines signal handlers for the 'home' app.

Automatically creates a Profile instance whenever a new User is created.
"""

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from home.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a Profile whenever a new User is created.

    Args:
        sender (Model): The model class sending the signal (User).
        instance (User): The actual instance being saved.
        created (bool): Whether this is a new instance.
        **kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)
