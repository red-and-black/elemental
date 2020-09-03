class BrowserError(Exception):
    """Raise when there is a problem with a browser operation."""


class NoSuchAttributeError(Exception):
    """Raise when an attribute cannot be found on an element."""


class NoSuchElementError(Exception):
    """Raise when an element cannot be found."""


class ParameterError(Exception):
    """Raise when there is a problem with parameters supplied to a function."""
