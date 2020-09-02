import pytest

from tests import utilities


@pytest.fixture
def test_actions_page(browser):
    url = utilities.build_url("test_actions.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_actions_page")
class TestClick:

    def test_button(self, browser):
        browser.get_element(id="button").click()
        element = browser.get_element(id="para-4")
        assert element.selenium_webelement.text == "Paragraph 4"
