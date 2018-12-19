"""Valid URL Configuration for testing purposes"""
from django.views.generic import RedirectView

GITHUB = RedirectView.as_view(
    url="https://github.com/jambonsw/django-url-check"
)
