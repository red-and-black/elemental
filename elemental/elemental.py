# pylint: disable=missing-function-docstring
import selenium
from selenium.webdriver.firefox import options as firefox_options

from elemental import (
    actions,
    getters,
    states,
    values,
)


class Common:
    """Base class to hold methods shared by the Browser and Element classes."""

    def get_button(self, **kwargs):  # noqa: D102
        return getters.get_button(self, **kwargs)

    def get_element(self, **kwargs):  # noqa: D102
        return getters.get_element(self, **kwargs)

    def get_elements(self, **kwargs):  # noqa: D102
        return getters.get_elements(self, **kwargs)

    def get_input(self, **kwargs):  # noqa: D102
        return getters.get_input(self, **kwargs)

    @property
    def html(self):  # noqa: D102
        return values.html(self)

    def screenshot(self, filepath):  # noqa: D102
        actions.screenshot(self, filepath)


class Browser(Common):
    """Represents a web browser.

    Parameters
    ----------
    selenium_webdriver : Selenium webdriver, optional
        The webdriver being used to drive the browser. Default is a Firefox
        WebDriver.
    headless : bool, optional
        Whether the default webdriver will run in headless mode. Has no effect
        if the default webdriver is not used. Default is False.

    Attributes
    ----------
    element_class : Element
        The Element class.
    selenium_webdriver : Selenium webdriver
        The webdriver being used to drive the browser.

    """

    def __init__(self, selenium_webdriver=None, headless=False):  # noqa: D107
        self.element_class = Element
        if selenium_webdriver:
            # If a webdriver is suppied, use it.
            self.selenium_webdriver = selenium_webdriver
        else:
            # Configure and use a Firefox webdriver if no webdriver is
            # supplied.
            options = firefox_options.Options()
            options.headless = headless
            self.selenium_webdriver = selenium.webdriver.Firefox(
                executable_path="geckodriver",
                options=options,
            )

    def quit(self):  # noqa: D102
        actions.quit(self)

    @property
    def title(self):  # noqa: D102
        return values.title(self)

    @property
    def url(self):  # noqa: D102
        return values.url(self)

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

    def attribute(self, attribute_name):  # noqa: D102
        return values.attribute(self, attribute_name)

    def check(self):  # noqa: D102
        actions.check(self)

    def click(self):  # noqa: D102
        actions.click(self)

    def fill(self, string):  # noqa: D102
        actions.fill(self, string)

    @property
    def is_displayed(self):  # noqa: D102
        return states.is_displayed(self)

    @property
    def is_enabled(self):  # noqa: D102
        return states.is_enabled(self)

    @property
    def is_selected(self):  # noqa: D102
        return states.is_selected(self)

    def select(self):  # noqa: D102
        actions.select(self)

    @property
    def text(self):  # noqa: D102
        return values.text(self)

    def uncheck(self):  # noqa: D102
        actions.uncheck(self)
