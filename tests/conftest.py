import pytest

from elemental import Browser


@pytest.fixture(scope="session")
def browser():
    """Browser fixture.

    Yields
    ------
    browser : browser
        A browser which wraps a Selenium webdriver.

    """
    # Create and yield the browser.
    _browser = Browser(headless=True)
    yield _browser

    # Stop the browser after the tests have finished.
    _browser.quit()
