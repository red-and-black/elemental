import pytest

from elemental import exceptions
from tests import utilities


@pytest.fixture
def test_getters_page(browser):
    url = utilities.build_url("test_getters.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_getters_page")
class TestGetParent:

    def test_parent_which_exists(self, browser):
        element = browser.get_element(id="wallaby").get_parent()
        assert element.attribute("id") == "select"


@pytest.mark.usefixtures("test_getters_page")
class TestGetParentErrors:

    def test_nonexistent_parent(self, browser):
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_element(tag="body").get_parent().get_parent()
        expected = "Parent not found for element: <html>"
        assert str(error.value) == expected

    def test_for_browser(self, browser):
        with pytest.raises(AttributeError) as error:
            browser.get_parent()
        expected = "'Browser' object has no attribute 'get_parent'"
        assert str(error.value) == expected

    def test_with_kwarg(self, browser):
        with pytest.raises(TypeError) as error:
            browser.get_element(id="select").get_parent(wait=3)
        expected = "get_parent() got an unexpected keyword argument 'wait'"
        assert str(error.value) == expected
