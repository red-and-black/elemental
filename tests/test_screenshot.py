import os

import pytest

from tests import utilities


@pytest.fixture
def test_actions_page(browser):
    url = utilities.build_url("test_actions.html")
    browser.visit(url)


@pytest.mark.usefixtures("test_actions_page")
class TestScreenshot:

    def test_browser(self, browser, tmpdir):
        filepath = os.path.join(str(tmpdir), "browser.png")
        browser.screenshot(filepath)
        assert os.path.isfile(filepath)

    def test_element(self, browser, tmpdir):
        filepath = os.path.join(str(tmpdir), "element.png")
        browser.get_element(id="screenshot").screenshot(filepath)
        assert os.path.isfile(filepath)
