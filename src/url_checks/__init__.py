"""Django Check ensures URL paths end with a slash"""
from .checks import check_url  # noqa: F401

__version__ = "0.2.0"
default_app_config = "url_checks.apps.UrlChecksConfig"
