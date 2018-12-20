"""Tests for django-url-check"""
import url_checks


def test_version():
    """Check that package has a version"""
    assert hasattr(url_checks, "__version__")
    assert isinstance(url_checks.__version__, str)
