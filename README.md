[![PyPI Version](https://img.shields.io/pypi/v/django-url-checks.svg)](https://pypi.org/project/django-url-checks/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-url-checks.svg)](https://pypi.org/project/django-url-checks/)
[![Django Versions](https://img.shields.io/pypi/djversions/django-url-checks.svg)](https://pypi.org/project/django-url-checks/)
[![Build Status](https://travis-ci.org/jambonsw/django-url-checks.svg?branch=development)](https://travis-ci.org/jambonsw/django-url-checks)
[![codecov](https://codecov.io/gh/jambonsw/django-url-checks/branch/development/graph/badge.svg)](https://codecov.io/gh/jambonsw/django-url-checks)
[![BCH compliance](https://bettercodehub.com/edge/badge/jambonsw/django-url-checks?branch=development)](https://bettercodehub.com/)

# Read Me

Use Django's System Check Framework to ensure your URL Configuration
works correctly.

## Table of Contents

- [Project Purpose](#project-purpose)
- [Project Rationale](#project-rationale)
- [Installation and Usage](#installation-and-usage)
- [Contributing](#contributing)

## Project Purpose

This package checks your Django project's URL Configuration for a few
things.

- Do the paths or regular expressions in your URL configuration tree end
  with slashes (or, for regular expressions, `/$`)
- Is the URL configuration tree comprised of only `URLPattern` and
  `URLResolver` instances (`path()` and `include()`)?
- Is `ROOT_URLCONF` defined in settings, and does it point to a valid
  Python module with `urlpatterns` defined?

[🔝 Up to Table of Contents](#table-of-contents)

## Project Rationale

I constantly forget to add a slash to the end of my URI paths. This
leads to strange behavior, and can be tricky to catch even with proper
testing.

What's more, the errors raised when something is amiss with the URL
configuration can be tricky to debug and understand.

As such, this package aim to try and make developers lives easier by
providing targeted checks of the URL configuration tree. This is meant
to be used as part of a "belt-and-braces" approach, and is not a
substitution for tests!

I am open to suggestions on improving the checks. Please open an issue
to do so.

[🔝 Up to Table of Contents](#table-of-contents)

## Installation and Usage

1. Add `"url_checks.apps.UrlChecksConfig",` as an item in your Django
   project's `INSTALLED_APPS` setting
2. In the terminal (in your Django projects code-root directory), run
   Django's check framework with `$ python manage.py check`
3. Read the output in your terminal and track those bugs down!

🎉

[🔝 Up to Table of Contents](#table-of-contents)

## Contributing

For ideas, bugs, feature-requests, and all the rest, please open an
[issue on Github](https://github.com/jambonsw/django-url-checks/issues).

[🔝 Up to Table of Contents](#table-of-contents)
