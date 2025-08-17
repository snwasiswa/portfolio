"""
apps.py

Defines the configuration for the 'home' app.
Includes automatic signal registration when the app is ready.
"""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the 'home' Django application.
    """

    name = 'home'

    def ready(self):
        """
        Called when the app is ready.

        Used to import and register signal handlers to ensure they are connected
        when the application starts.
        """
        import home.signals  # noqa
