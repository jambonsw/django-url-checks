"""Tests for django-url-check"""
import django_url_check


def test_version():
    """Check that package has a version"""
    assert hasattr(django_url_check, "__version__")
    assert isinstance(django_url_check.__version__, str)
