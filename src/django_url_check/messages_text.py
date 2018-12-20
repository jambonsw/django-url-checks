"""Text constants to be used in messages"""
from typing import NamedTuple, Optional

__all__ = ["CRITICAL_PROTO_MSG", "ERROR_PROTO_MSG"]


class ProtoMsg(NamedTuple):
    """Prototype Message, for generating IDs automatically"""

    var: str  # variable attribute name
    msg: str  # string message
    hint: Optional[str]  # hint


BASIC_URLCONF_MSG = (
    "Define ROOT_URLCONF in your settings as a string pointing to your"
    ' URL paths (e.g.: ROOT_URLCONF="config.urls")'
)

CRITICAL_PROTO_MSG = [
    ProtoMsg(
        "URLCONF_NOT_DEFINED",
        "Root UrlConf setting not defined",
        BASIC_URLCONF_MSG,
    ),
    ProtoMsg(
        "URLCONF_WRONG_FORMAT",
        "Root UrlConf setting unexpected format",
        BASIC_URLCONF_MSG,
    ),
    ProtoMsg(
        "URLCONF_NOT_FOUND",
        "Root UrlConf module not found",
        "Point ROOT_URLCONF in your settings to an existing module in your"
        ' code (e.g.: ROOT_URLCONF="config.urls" points Django to '
        "<project_root>/config/urls.py)",
    ),
    ProtoMsg(
        "URLCONF_NO_PATTERNS",
        "Root UrlConf missing urlpatterns",
        "Your root URL configuration must contain a variable named"
        " urlpatterns with a list of URL paths.  (e.g.: urlpatterns=["
        'path("", home_view, name="home")]',
    ),
    ProtoMsg(
        "URLCONF_UNKNOWN_TYPE",
        "Your URL configuration tree contains an unknwon type."
        " Only expected use of path() and include()",
        None,
    ),
]

ERROR_PROTO_MSG = [
    ProtoMsg("NO_SLASH_PATTERN", "URI pattern does not end with slash", None),
    ProtoMsg(
        "NO_SLASH_RESOLVER",
        "URI include pattern does not end with slash",
        None,
    ),
]
