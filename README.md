[![PyPI Version](https://img.shields.io/pypi/v/django-url-checks.svg)](https://pypi.org/project/django-url-checks/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-url-checks.svg)](https://pypi.org/project/django-url-checks/)
[![Django Versions](https://img.shields.io/pypi/djversions/django-url-checks.svg)](https://pypi.org/project/django-url-checks/)
[![Build Status](https://travis-ci.org/jambonsw/django-url-checks.svg?branch=development)](https://travis-ci.org/jambonsw/django-url-checks)
[![codecov](https://codecov.io/gh/jambonsw/django-url-checks/branch/development/graph/badge.svg)](https://codecov.io/gh/jambonsw/django-url-checks)
[![BCH compliance](https://bettercodehub.com/edge/badge/jambonsw/django-url-checks?branch=development)](https://bettercodehub.com/)

# Read Me

Even with proper testing, it's easy to accidentally forget a slash at
the end of a URI path in Django's URL configuration, which in turn can
lead to unexpected behavior. This Django check helps follow a
belt-and-braces approach and will verify that all paths (endpoints and
includes) end with a slash (or, for regular expressions, `"/$"`).

I am open to suggestions on improving the check. Please open an issue to
do so.
