import pytest

from tests import utilities


@pytest.fixture
def test_values_page(browser):
    url = utilities.build_url("test_values.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_values_page")
class TestHtml:

    def test_empty_span(self, browser):
        expected = "<span id=\"span-1\"></span>"
        assert browser.get_element(id="span-1").html == expected

    def test_head(self, browser):
        html = browser.get_element(tag="head").html
        assert html.startswith("<head>")
        assert html.endswith("</head>")

    def test_paragraph(self, browser):
        expected = (
            "<p id=\"para-2\">A paragraph with trailing whitespace.  </p>"
        )
        assert browser.get_element(id="para-2").html == expected

    def test_span_containing_whitespace(self, browser):
        expected = "<span id=\"span-2\"> </span>"
        assert browser.get_element(id="span-2").html == expected

    def test_whole_page(self, browser):
        html = browser.html
        assert html.startswith("<html>")
        assert html.endswith("</html>")
