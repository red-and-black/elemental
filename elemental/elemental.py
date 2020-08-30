# pylint: disable=missing-function-docstring
from elemental import (
    actions,
    getters,
)


class Common:
    """Base class to hold methods shared by the Browser and Element classes."""

    def get_element(self, **kwargs):  # noqa: D102
        return getters.get_element(self, **kwargs)

    def get_elements(self, **kwargs):  # noqa: D102
        return getters.get_elements(self, **kwargs)


class Browser(Common):
    """Represents a web browser.

    Parameters
    ----------
    selenium_webdriver : Selenium webdriver
        The webdriver being used to drive the browser.

    Attributes
    ----------
    element_class : Element
        The Element class.
    selenium_webdriver : Selenium webdriver
        The webdriver being used to drive the browser.

    """

    def __init__(self, selenium_webdriver):  # noqa: D107
        self.element_class = Element
        self.selenium_webdriver = selenium_webdriver

    def quit(self):  # noqa: D102
        actions.quit(self)

    def visit(self, url):  # noqa: D102
        actions.visit(self, url)


class Element(Common):
    """Represents an HTML element.

    Parameters
    ----------
    selenium_webdriver : Selenium webdriver
        The webdriver being use to drive the browser.
    selenium_webelement : Selenium webelement, optional
        The webelement for the HTML element. This is supplied for an
        Element instance, and is not supplied for a Browser instance.

    Attributes
    ----------
    element_class : Element
        The Element class.
    selenium_webdriver : Selenium webdriver
        The webdriver being used to drive the browser.
    selenium_webelement : Selenium webelement
        The webelement for the HTML element.

    """

    def __init__(self, selenium_webdriver,
                 selenium_webelement=None):  # noqa: D107
        self.element_class = Element
        self.selenium_webdriver = selenium_webdriver
        self.selenium_webelement = selenium_webelement
