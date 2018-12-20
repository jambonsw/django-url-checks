"""AppConfig for django-url-checks package"""
from django.apps import AppConfig


class UrlChecksConfig(AppConfig):
    """AppConfig for django-url-checks package"""

    name = "url_checks"

    def ready(self):
        """Import checks once apps are loaded

        Note that the register decorator does the actual work of
        informing Django about the check.
        """
        from .checks import check_url  # noqa: F401
