"""Valid URL Configuration for testing purposes"""
from django.urls import include, path, re_path

from .views import GITHUB

nested_urlpatterns = [
    path("", GITHUB, name="nested_home"),
    path("g1/", GITHUB, name="nested_1"),
]

urlpatterns = [
    path("", GITHUB, name="home"),
    path("g1", GITHUB, name="github1"),
    re_path(r"^g2/$", GITHUB, name="github2"),
    path("more1/", include(nested_urlpatterns)),
    re_path(r"^more2/", include(nested_urlpatterns)),
    path(
        "more3/", include((nested_urlpatterns, "more3_app"), namespace="more3")
    ),
    re_path(
        r"^more4/",
        include((nested_urlpatterns, "more4_app"), namespace="more4"),
    ),
]
