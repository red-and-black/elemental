from selenium.common import exceptions as selenium_exceptions

from elemental import exceptions


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
