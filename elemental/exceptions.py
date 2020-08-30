class BrowserError(Exception):
    """Raise when there is a problem with a browser operation."""


class NoSuchElementError(Exception):
    """Raise when an element cannot be found."""


class ParameterError(Exception):
    """Raise when there is a problem with parameters supplied to a function."""
