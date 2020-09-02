from selenium.common import exceptions as selenium_exceptions

from elemental import exceptions


def check(element):
    """Check a checkbox.

    Always leaves the checkbox element in a 'checked' state. Uses Selenium's
    WebElement.click()

    Parameters
    ----------
    element : element
        The checkbox element.

    Returns
    -------
    None

    """
    if not element.selenium_webelement.is_selected():
        element.selenium_webelement.click()


def click(element):
    """Click an element.

    This is a wrapper for Selenium's WebElement.click()

    Parameters
    ----------
    element : element
        The element to click.

    Returns
    -------
    None

    """
    element.selenium_webelement.click()


def fill(element, string):
    """Fill an input with text or a filepath.

    Uses Selenium's WebElement.send_keys()

    Parameters
    ----------
    element : element
        The input element.
    string : str
        The string to give the input field.

    Returns
    -------
    None

    """
    element.selenium_webelement.clear()
    element.selenium_webelement.send_keys(string)


def quit(browser):  # pylint: disable=redefined-builtin
    """Quit the Selenium webdriver and close the browser windows.

    This is a wrapper for Selenium's WebDriver.quit()

    Parameters
    ----------
    browser : browser
        The browser.

    Returns
    -------
    None

    """
    browser.selenium_webdriver.quit()


def screenshot(parent, filepath):
    """Click an element.

    This is a wrapper for Selenium's WebElement.screenshot() and
    WedDriver.save_screenshot()

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    filepath : str
        The full filepath for saving the file.

    Returns
    -------
    None

    """
    if isinstance(parent, parent.element_class):
        parent.selenium_webelement.screenshot(filepath)
    else:
        parent.selenium_webdriver.save_screenshot(filepath)


def select(element):
    """Select a select option or radio button.

    Always leaves the option or radio button element in a 'selected' state.
    Uses Selenium's WebElement.click()

    Parameters
    ----------
    element : element
        The option or radio button element.

    Returns
    -------
    None

    """
    if not element.selenium_webelement.is_selected():
        element.selenium_webelement.click()


def uncheck(element):
    """Uncheck a checkbox.

    Always leaves the checkbox element in an 'unchecked' state. Uses Selenium's
    WebElement.click()

    Parameters
    ----------
    element : element
        The checkbox element.

    Returns
    -------
    None

    """
    if element.selenium_webelement.is_selected():
        element.selenium_webelement.click()


def visit(browser, url):
    """Navigate to a URL.

    This is a wrapper for Selenium's WebDriver.get()

    Parameters
    ----------
    browser : browser
        The browser.
    url : string
        The URL to navigate to.

    Returns
    -------
    None

    """
    try:
        browser.selenium_webdriver.get(url)
    except selenium_exceptions.WebDriverException as error:
        raise exceptions.BrowserError(error)
