import pytest

from tests import utilities


@pytest.fixture
def test_values_page(browser):
    url = utilities.build_url("test_values.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_values_page")
class TestText:

    def test_empty_span(self, browser):
        assert browser.get_element(tag="span").text == ""

    def test_paragraph(self, browser):
        expected = "This is the contents test page."
        assert browser.get_element(tag="p").text == expected

    def test_paragraph_with_trailing_whitespace(self, browser):
        expected = "A paragraph with trailing whitespace."
        assert browser.get_element(tag="p", occurrence=2).text == expected

    def test_span_containing_only_whitespace(self, browser):
        assert browser.get_element(tag="span", occurrence=2).text == ""
