import pytest

from tests import utilities


@pytest.fixture
def test_actions_page(browser):
    url = utilities.build_url("test_actions.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_actions_page")
class TestCheck:

    def test_prechecked_box(self, browser):
        element = browser.get_element(id="unchecking")
        assert element.selenium_webelement.is_selected()
        element.check()
        assert element.selenium_webelement.is_selected()

    def test_unchecked_box(self, browser):
        element = browser.get_element(id="checking")
        assert not element.selenium_webelement.is_selected()
        element.check()
        assert element.selenium_webelement.is_selected()
