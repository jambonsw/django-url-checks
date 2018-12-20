"""Tests for utility functions in-use by package"""
from django.core.checks import (
    Critical,
    Debug,
    Error,
    Info,
    Warning as CheckWarning,
)
from pytest import mark, param

from django_url_check.messages import get_message_letter


@mark.parametrize(
    "Message, letter",
    [
        (Critical, "C"),
        (Debug, "D"),
        (Error, "E"),
        (Info, "I"),
        (CheckWarning, "W"),
        param(None, None, marks=mark.xfail(exception=KeyError)),
    ],
)
def test_message_letter(Message, letter):
    """Does the utility return the letter Django expects?"""
    assert get_message_letter(Message) == letter
