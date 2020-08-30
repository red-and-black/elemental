import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from elemental.elemental import Browser


@pytest.fixture(scope="session")
def browser():
    """Browser fixture.

    Yields
    ------
    browser : browser
        A browser which wraps a Selenium webdriver.

    """
    # Create and configure the Selenium webdriver.
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(executable_path='geckodriver', options=options)

    # Create and yield the browser.
    _browser = Browser(driver)
    yield _browser

    # Stop the Selenium webdriver after the tests have finished.
    _browser.quit()
