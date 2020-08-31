import pytest

from tests import utilities


@pytest.fixture
def test_states_page(browser):
    url = utilities.build_url("test_states.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_states_page")
class TestIsEnabled:

    def test_checkbox(self, browser):
        # Test a disabled element.
        assert not browser.get_element(id="terms").is_enabled

        # Test an enabled element.
        assert browser.get_element(id="checking").is_enabled

    def test_option(self, browser):
        # Test a disabled element.
        assert not browser.get_element(id="wombat").is_enabled

        # Test an enabled element.
        assert browser.get_element(id="kangaroo").is_enabled

    def test_radio_button(self, browser):
        # Test a disabled element.
        assert not browser.get_element(id="green").is_enabled

        # Test an enabled element.
        assert browser.get_element(id="blue").is_enabled
