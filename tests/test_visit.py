import pytest

from elemental import exceptions
from tests import utilities


class TestVisit:

    def test_good_url(self, browser):
        url = utilities.build_url("test_actions.html")
        browser.visit(url)
        assert browser.selenium_webdriver.title == "Actions test page"


class TestVisitErrors:

    def test_nonexistent_url(self, browser):
        nonexistent_url = utilities.build_url("abc.html")
        with pytest.raises(exceptions.BrowserError) as error:
            browser.visit(nonexistent_url)
        expected = "Message: Reached error page"
        assert str(error.value).startswith(expected)
