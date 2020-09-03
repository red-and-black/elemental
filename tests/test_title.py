from tests import utilities


class TestTitle:

    def test_good_url(self, browser):
        url = utilities.build_url("test_values.html")
        browser.selenium_webdriver.get(url)
        assert browser.title == "Values test page"
