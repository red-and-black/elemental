from elemental import exceptions


def attribute(element, attribute_name):
    """Get the value of an attribute of an element.

    This is a wrapper for Selenium's WebElement.get_attribute()

    Parameters
    ----------
    element : element
        The element.
    attribute_name : str
        The name of the attribute.

    Returns
    -------
    str or bool
        The value of the attribute.

    Raises
    ------
    NoSuchAttributeError
        When the attribute cannot be found on the element.

    """
    attribute_value = element.selenium_webelement.get_attribute(attribute_name)

    # Test for None rather than falsy because the value of an attribute can be
    # an empty string, and if it is, that should be returned rather than
    # causing an exception.
    if attribute_value is None:
        error = "Attribute not found: {}".format(attribute_name)
        raise exceptions.NoSuchAttributeError(error)

    return attribute_value


def html(parent):
    """Get the HTML of an element or page.

    This is a wrapper for Selenium's WebDriver.page_source and
    WebElement.get_attribute("outerHTML")

    Parameters
    ----------
    parent : browser or element
        The browser or element.

    Returns
    -------
    str
        If parent is a browser, the HTML of the whole page.
        If parent is an element, the HTML of the element.

    """
    if isinstance(parent, parent.element_class):
        return parent.selenium_webelement.get_attribute("outerHTML")
    return parent.selenium_webdriver.page_source


def text(element):
    """Get the text contained by an element.

    This is a wrapper for Selenium's WebElement.text

    Parameters
    ----------
    element : element
        The element.

    Returns
    -------
    str
        The text of the element.

    """
    return element.selenium_webelement.text


def title(browser):
    """Get the title of the page.

    This is a wrapper for Selenium's WebDriver.title

    Parameters
    ----------
    browser : browser
        The browser.

    Returns
    -------
    str
        The title of the page.

    """
    return browser.selenium_webdriver.title


def url(browser):
    """Get the url of the page.

    This is a wrapper for Selenium's WebDriver.current_url

    Parameters
    ----------
    browser : browser
        The browser.

    Returns
    -------
    str
        The url of the page.

    """
    return browser.selenium_webdriver.current_url
