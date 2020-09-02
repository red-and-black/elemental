import pytest

from tests import utilities


@pytest.fixture
def test_actions_page(browser):
    url = utilities.build_url("test_actions.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_actions_page")
class TestSelect:

    def test_option(self, browser):
        element = browser.get_element(id="wombat")
        assert not element.selenium_webelement.is_selected()
        element.select()
        assert element.selenium_webelement.is_selected()

    def test_radio_button(self, browser):
        element = browser.get_element(id="radio_one")
        assert not element.selenium_webelement.is_selected()
        element.select()
        assert element.selenium_webelement.is_selected()
