"""Test behavior around Django settings"""
from django.core.checks import Critical
from pytest import mark, param

from django_url_check import check_url
from django_url_check.messages import MESSAGES


@mark.parametrize(
    "message_name",
    [
        param(
            "URLCONF_NOT_DEFINED", marks=mark.delete_settings("ROOT_URLCONF")
        ),
        param(
            "URLCONF_WRONG_FORMAT",
            marks=mark.override_settings(ROOT_URLCONF=None),
            id="URLCONF_as_None",
        ),
        param(
            "URLCONF_WRONG_FORMAT",
            marks=mark.override_settings(ROOT_URLCONF=9),
            id="URLCONF_as_int",
        ),
        param(
            "URLCONF_NOT_FOUND",
            marks=mark.override_settings(ROOT_URLCONF="nonexistent.urls"),
        ),
        param(
            "URLCONF_NO_PATTERNS",
            marks=mark.override_settings(ROOT_URLCONF="tests.conftest"),
        ),
    ],
)
def test_root_url_settings(message_name):
    """Ensure errors are raised for misconfigurations"""
    messages = check_url()
    assert len(messages) == 1, "Only one message should be returned"
    msg = messages[0]
    assert isinstance(msg, Critical) is True, "Wrong Message level used"
    expected_msg = getattr(MESSAGES, message_name)().msg
    assert msg.msg == expected_msg, "Wrong Message displayed"
    assert msg.hint is not None, "Hint should be provided"
