"""All of the messages used by the check"""
from functools import partial

from django.core.checks import (
    Critical,
    Debug,
    Error,
    Info,
    Warning as CheckWarning,
)

from .messages_text import CRITICAL_PROTO_MSG, ERROR_PROTO_MSG

__all__ = ["MESSAGES"]


def get_message_letter(Message):
    """Return expected character code for Django Message"""
    if Message is Critical:
        return "C"
    elif Message is Error:
        return "E"
    elif Message is CheckWarning:
        return "W"
    elif Message is Info:
        return "I"
    elif Message is Debug:
        return "D"
    else:
        raise KeyError()


def omit_keys(*args):
    """Remove keys from a dictionary"""
    *keys, dict_obj = args
    return {
        field: value for field, value in dict_obj.items() if field not in keys
    }


def build_messages(app_name, Message, message_list):
    """Build messages dictionary of specific type"""
    letter = get_message_letter(Message)
    return {
        msg.var: partial(
            Message,
            id=f"{app_name}.{letter}{i:0{3}}",
            **omit_keys("var", msg._asdict()),
        )
        for i, msg in enumerate(message_list, start=1)
    }


class Messages:
    """Singleton container for all messages"""

    def __init__(self, app_name="url_checks"):
        self._messages = dict(  # this construction ensures no duplicate keys
            **build_messages(app_name, Critical, CRITICAL_PROTO_MSG),
            **build_messages(app_name, Error, ERROR_PROTO_MSG),
        )

    def __getattr__(self, name):
        if name in self._messages:
            return self._messages[name]
        raise AttributeError(name)


MESSAGES = Messages()
