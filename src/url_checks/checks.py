"""Django Check ensures URL paths end with a slash

https://docs.djangoproject.com/en/2.1/topics/checks/
"""
from importlib import import_module

from django.conf import settings
from django.core.checks import register
from django.urls import URLPattern, URLResolver

from .messages import MESSAGES

__all__ = ["check_url"]


def _get_url_tree():
    """Get Root URL Configuration for project"""
    try:
        url_mod_dot_path = settings.ROOT_URLCONF
    except AttributeError:
        return (None, [MESSAGES.URLCONF_NOT_DEFINED()])
    try:
        url_mod = import_module(url_mod_dot_path)
    except AttributeError:
        return (None, [MESSAGES.URLCONF_WRONG_FORMAT()])
    except ModuleNotFoundError:
        return (None, [MESSAGES.URLCONF_NOT_FOUND()])
    try:
        return (url_mod.urlpatterns, None)
    except AttributeError:
        return (None, [MESSAGES.URLCONF_NO_PATTERNS()])


def _check_path(path, namespace):
    """Verify that a single path ends with a slash"""
    pattern = str(path.pattern)
    if len(pattern) > 0 and not pattern.endswith(("/", "/$")):
        name = f"{namespace}:{path.name}" if namespace else path.name
        return MESSAGES.NO_SLASH_PATTERN(
            hint=f'Add slash to end of path "{pattern}", named "{name}"'
        )


def _check_resolver(path, namespace):
    """Verify that an include path ends with a slash"""
    pattern = str(path.pattern)
    if len(pattern) > 0 and not pattern.endswith(("/", "/$")):
        return MESSAGES.NO_SLASH_RESOLVER(
            hint=f'Add slash to end of include path "{pattern}"'
        )


def _check_path_tree(url_tree, namespace=None):
    """Provide error for each URI pattern missing a / at end"""
    errors = []
    for path in url_tree:
        if isinstance(path, URLPattern):
            msg = _check_path(path, namespace)
            if msg:
                errors.append(msg)
        elif isinstance(path, URLResolver):
            new_namespace = (
                f"{namespace}:{path.namespace}"
                if namespace and path.namespace
                else (path.namespace or namespace)
            )
            msg = _check_resolver(path, namespace)
            if msg:
                errors.append(msg)
            errors.extend(_check_path_tree(path.url_patterns, new_namespace))
        else:
            errors.append(MESSAGES.URLCONF_UNKNOWN_TYPE())
    return errors


@register()
def check_url(*args, **kwargs):
    """Ensure all URI paths end with a '/' character"""
    url_tree, messages = _get_url_tree()
    return messages or _check_path_tree(url_tree)
