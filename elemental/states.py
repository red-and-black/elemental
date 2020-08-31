def is_displayed(element):
    """Determine if an element is displayed.

    This is a wrapper around Selenium's WebElement.is_displayed(). Note it does
    not work on hidden select options.

    Parameters
    ----------
    element : element
        The element to test.

    Returns
    -------
    bool
        True if displayed, False otherwise.

    """
    return element.selenium_webelement.is_displayed()


def is_enabled(element):
    """Determine if an element is enabled.

    This is a wrapper around Selenium's WebElement.is_enabled()

    Parameters
    ----------
    element : element
        The element to test.

    Returns
    -------
    bool
        True if enabled, False otherwise.

    """
    return element.selenium_webelement.is_enabled()


def is_selected(element):
    """Determine if an option, radio button or checkbox is selected.

    This is a wrapper around Selenium's WebElement.is_selected().

    Parameters
    ----------
    element : element
        The option, checkbox or radio button element to test.

    Returns
    -------
    bool
        True if selected, False otherwise.

    """
    return element.selenium_webelement.is_selected()
