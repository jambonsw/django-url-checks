"""Tests for django-url-check"""
from django_url_check import __version__


def test_version():
    """Check that package has a version"""
    assert __version__ == "0.1.0"
