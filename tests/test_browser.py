import selenium
from selenium.webdriver.firefox import options as firefox_options

from elemental import Browser
from tests import utilities


def test_nondefault_browser():
    # Create and configure the browser.
    options = firefox_options.Options()
    options.headless = True
    selenium_webdriver = selenium.webdriver.Firefox(
        executable_path="geckodriver",
        options=options,
    )
    browser = Browser(selenium_webdriver)

    # Test the the browser.
    url = utilities.build_url("test_actions.html")
    browser.visit(url)
    assert browser.title == "Actions test page"

    # Stop the browser.
    browser.quit()
