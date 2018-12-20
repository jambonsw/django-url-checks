"""Tests for django-url-check"""
import url_checks


def test_version():
    """Check that package has a version"""
    assert hasattr(url_checks, "__version__")
    assert isinstance(url_checks.__version__, str)


def test_default_app():
    """Check that package has a default Django app

    https://docs.djangoproject.com/en/stable/ref/applications/#configuring-applications
    """
    assert hasattr(url_checks, "default_app_config")
    assert isinstance(url_checks.default_app_config, str)
