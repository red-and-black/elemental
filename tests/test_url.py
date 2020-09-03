from tests import utilities


class TestUrl:

    def test_good_url(self, browser):
        url = utilities.build_url("test_values.html")
        browser.selenium_webdriver.get(url)
        assert browser.url == url
