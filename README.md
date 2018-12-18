# Read Me

Even with proper testing, it's easy to accidentally forget a slash at
the end of a URI path in Django's URL configuration, which in turn can
lead to unexpected behavior. This Django check helps follow a
belt-and-braces approach and will verify that all paths (endpoints and
includes) end with a slash (or, for regular expressions, `"/$"`).

I am open to suggestions on improving the check. Please open an issue to
do so.
