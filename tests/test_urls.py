"""Test behavior around URIs"""
from re import compile as re_compile, search

from django.core.checks import Error
from pytest import mark

from django_url_check import check_url
from django_url_check.messages import MESSAGES


def test_valid_check():
    """Ensure valid URIs don't return messages"""
    messages = check_url()
    assert len(messages) == 0, "No messages should be returned"


def _test_invalid(settings, urlconf, message_name):
    """Test utility used for all URI paths

    This is where most of the test code is, as the tests for both
    URLPatterns and URLResolvers are nearly identical
    """
    settings.ROOT_URLCONF = f"tests.fixtures.{urlconf}"
    messages = check_url()
    msg = messages[0]
    assert len(messages) == 1, "One message should be returned"
    assert isinstance(msg, Error) is True, "Wrong Message level used"
    expected_msg = getattr(MESSAGES, message_name)().msg
    assert msg.msg == expected_msg, "Wrong Message displayed"
    assert msg.hint is not None, "Hint should be provided"
    assert isinstance(msg.hint, str), "Hint should be a string"
    return msg


@mark.parametrize(
    "urlconf, name",
    [("invalid_path", "github1"), ("invalid_re_path", "github2")],
)
def test_invalid_path(settings, urlconf, name):
    """Do we return messages when slash is missing from URLPatterns?"""
    message = _test_invalid(settings, urlconf, "NO_SLASH_PATTERN")
    assert search(
        f'named "{name}"$', message.hint
    ), f'Hint "{message.hint}" does not provide name of path'


@mark.parametrize(
    "urlconf, path",
    [
        ("invalid_include_namespace", "more3"),
        ("invalid_include", "more1"),
        ("invalid_re_include_namespace", r"\^more4"),
        ("invalid_re_include", r"\^more2"),
    ],
)
def test_invalid_include(settings, urlconf, path):
    """Do we return messages when slash is missing from URLResolver?"""
    message = _test_invalid(settings, urlconf, "NO_SLASH_RESOLVER")
    assert search(
        f'include path "{path}"$', message.hint
    ), f'Hint "{message.hint}" does not provide name of path'


@mark.override_settings(ROOT_URLCONF="tests.fixtures.invalid_nested_path")
def test_invalid_nested_path():
    """Single path nested multiple times returns multiple messages"""
    message_list = check_url()
    expected_msg = MESSAGES.NO_SLASH_PATTERN().msg
    pattern = re_compile('named "(more[34]:)?nested_1"$')
    assert len(message_list) == 4, "4 includes should result in 4 messages" ""
    for message in message_list:
        assert isinstance(message, Error) is True, "Wrong Message level used"
        assert message.msg == expected_msg, "Wrong Message displayed"
        assert pattern.search(
            message.hint
        ), f'Hint "{message.hint}" does not provide name of path'
