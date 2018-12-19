"""PyTest Configuration"""
from django.conf import settings
from pytest import fixture
from pytest_django.lazy_django import skip_if_no_django


def pytest_configure():
    """Configure Django settings"""
    settings.configure(
        SITE_ID=1,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.messages",
            "django.contrib.sessions",
            "django.contrib.sites",
        ],
        MIDDLEWARE=[
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ],
        ROOT_URLCONF="tests.fixtures.valid_urls",
    )


@fixture(autouse=True, scope="function")
def _delete_settings(request):
    marker = request.node.get_closest_marker("delete_settings")
    if marker:
        skip_if_no_django()
        from django.conf import settings

        original_settings = {}
        for arg in marker.args:
            if hasattr(settings, arg):
                original_settings[arg] = getattr(settings, arg)
                delattr(settings, arg)

        def restore():
            for setting_name, value in original_settings.items():
                setattr(settings, setting_name, value)

        request.addfinalizer(restore)


@fixture(autouse=True, scope="function")
def _override_settings(request):
    marker = request.node.get_closest_marker("override_settings")
    if marker:
        skip_if_no_django()
        from django.conf import settings

        original_settings = {}
        for setting_name, value in marker.kwargs.items():
            if hasattr(settings, setting_name):
                original_settings[setting_name] = getattr(
                    settings, setting_name
                )
            setattr(settings, setting_name, value)

        if original_settings:

            def restore():
                for setting_name, value in original_settings.items():
                    setattr(settings, setting_name, value)

            request.addfinalizer(restore)
