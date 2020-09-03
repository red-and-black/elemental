import pytest

from tests import utilities


@pytest.fixture
def test_states_page(browser):
    url = utilities.build_url("test_states.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_states_page")
class TestIsSelected:

    def test_checkbox(self, browser):
        # Test element which isn't selected.
        element = browser.get_element(id="checking")
        assert not element.is_selected

        # Test selected element.
        element.selenium_webelement.click()
        assert element.is_selected

    def test_option(self, browser):
        # Test element which isn't selected.
        element = browser.get_element(id="wallaby")
        assert not element.is_selected

        # Test selected element.
        element.selenium_webelement.click()
        assert element.is_selected

    def test_paragraph(self, browser):
        assert not browser.get_element(tag="p").is_selected

    def test_radio_button(self, browser):
        # Test element which isn't selected.
        element = browser.get_element(id="purple")
        assert not element.is_selected

        # Test selected element.
        element.selenium_webelement.click()
        assert element.is_selected
