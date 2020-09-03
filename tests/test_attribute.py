import pytest

from elemental import exceptions
from tests import utilities


@pytest.fixture
def test_values_page(browser):
    url = utilities.build_url("test_values.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_values_page")
class TestAttribute:

    def test_class_attribute(self, browser):
        assert browser.get_element(tag="h1").attribute("class") == "heading"

    def test_empty_attribute(self, browser):
        assert browser.get_element(tag="h1").attribute("id") == ""

    def test_hidden_attribute(self, browser):
        assert browser.get_element(id="hidden-para").attribute("hidden")

    def test_id_attribute(self, browser):
        assert browser.get_element(tag="p").attribute("id") == "para-1"

    def test_missing_class_attribute(self, browser):
        # The desired behaviour when the class attribute is missing is for a
        # NoSuchAttributeError to be raised, but instead an empty string is
        # returned. This test is simply to monitor this behaviour to see if it
        # ever changes.
        assert browser.get_element(tag="p").attribute("class") == ""


@pytest.mark.usefixtures("test_values_page")
class TestAttributeErrors:

    def test_no_parameter(self, browser):
        with pytest.raises(TypeError) as error:
            browser.get_element(tag="p").attribute()
        expected = "attribute() missing 1 required positional argument"
        assert str(error.value).startswith(expected)

    def test_nonexistent_attribute(self, browser):
        with pytest.raises(exceptions.NoSuchAttributeError) as error:
            browser.get_element(tag="p").attribute("name")
        expected = "Attribute not found: name"
        assert str(error.value) == expected
