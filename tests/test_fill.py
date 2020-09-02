import pytest

from tests import utilities


@pytest.fixture
def test_actions_page(browser):
    url = utilities.build_url("test_actions.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_actions_page")
class TestFill:

    def test_text_input(self, browser):
        element = browser.get_element(id="text_input")
        element.fill("Sometext")
        assert element.selenium_webelement.get_attribute("value") == "Sometext"
