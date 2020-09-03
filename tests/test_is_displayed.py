import pytest

from tests import utilities


@pytest.fixture
def test_states_page(browser):
    url = utilities.build_url("test_states.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_states_page")
class TestIsDisplayed:

    def test_paragraph(self, browser):
        # Test a hidden element.
        assert not browser.get_element(id="hiding").is_displayed

        # Test a displayed element.
        assert browser.get_element(tag="p").is_displayed

    def test_radio_button(self, browser):
        # Test a hidden element.
        assert not browser.get_element(id="orange").is_displayed

        # Test a displayed element.
        assert browser.get_element(id="purple").is_displayed
