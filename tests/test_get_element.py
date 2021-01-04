import pytest

from elemental import exceptions
from tests import utilities


@pytest.fixture
def test_getters_page(browser):
    url = utilities.build_url("test_getters.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_getters_page")
class TestGetElement:

    def test_by_class_name(self, browser):
        element = browser.get_element(class_name="link")
        actual = element.selenium_webelement.text
        assert actual == "Python Package Index (PyPI)"

    def test_by_css(self, browser):
        element = browser.get_element(css="div.container p")
        assert element.selenium_webelement.text == "Paragraph 3"

    def test_by_id(self, browser):
        element = browser.get_element(id="heading")
        assert element.selenium_webelement.text == "Heading"

    def test_by_link_text(self, browser):
        element = browser.get_element(link_text="Python Package Index (PyPI)")
        actual = element.selenium_webelement.text
        assert actual == "Python Package Index (PyPI)"

    def test_by_name(self, browser):
        element = browser.get_element(name="para-1")
        assert element.selenium_webelement.text == "Paragraph 1"

    def test_by_partial_link_text(self, browser):
        element = browser.get_element(partial_link_text="PyPI")
        actual = element.selenium_webelement.text
        assert actual == "Python Package Index (PyPI)"

    def test_by_partial_text(self, browser):
        element = browser.get_element(partial_text="I'm \"Paragraph")
        assert element.selenium_webelement.text == "I'm \"Paragraph 2\""

    def test_by_tag(self, browser):
        element = browser.get_element(tag="a")
        actual = element.selenium_webelement.text
        assert actual == "Python Package Index (PyPI)"

    def test_by_text(self, browser):
        # Test without quotes.
        element = browser.get_element(text="Python.org")
        assert element.selenium_webelement.text == "Python.org"

        # Test with single and double quotes.
        element = browser.get_element(text="I'm \"Paragraph 2\"")
        assert element.selenium_webelement.text == "I'm \"Paragraph 2\""

    def test_by_type(self, browser):
        element = browser.get_element(type="button")
        assert element.selenium_webelement.text == "Add paragraph"

    def test_by_value(self, browser):
        element = browser.get_element(value="Wallaby")
        assert element.selenium_webelement.text == "Wallaby"

    def test_by_xpath(self, browser):
        element = browser.get_element(xpath="//*[@id='para-2']")
        assert element.selenium_webelement.text == "I'm \"Paragraph 2\""

    def test_chaining(self, browser):
        # Ensure that 'partial_text' finds from the element and not the page
        # root.
        element = browser.\
            get_element(class_name="container").\
            get_element(partial_text="Paragraph")
        assert element.selenium_webelement.text == "Paragraph 3"

        # Ensure that 'text' finds from the element and not the page root.
        element = browser.\
            get_element(class_name="container").\
            get_element(text="Paragraph 3")
        assert element.selenium_webelement.text == "Paragraph 3"

    def test_no_waiting(self, browser):
        element = browser.get_element(id="heading", wait=0)
        assert element.selenium_webelement.text == "Heading"

    def test_occurrence(self, browser):
        element = browser.get_element(tag="p", occurrence=3)
        assert element.selenium_webelement.text == "Paragraph 3"

    def test_waiting(self, browser):
        browser.selenium_webdriver.find_element_by_tag_name("button").click()
        element = browser.get_element(id="para-4")
        assert element.selenium_webelement.text == "Paragraph 4"


@pytest.mark.usefixtures("test_getters_page")
class TestGetElementErrors:

    def test_forbidden_occurrence(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(id="heading", occurrence=0)
        expected = "The 'occurrence' parameter cannot be less than 1"
        assert str(error.value) == expected

    def test_forbidden_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(id="heading", wait=-2)
        expected = "The 'wait' parameter cannot be less than 0"
        assert str(error.value) == expected

    def test_insufficient_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element()
        expected = (
            "One parameter from this list is required: class_name, css, id, "
            "link_text, name, partial_link_text, partial_text, tag, text, "
            "type, value, xpath"
        )
        assert str(error.value) == expected

    def test_nonexistent_element(self, browser):
        # Without specifying the occurrence.
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_element(id="abc", wait=0)
        expected = "Element not found: id=\"abc\""
        assert str(error.value) == expected

        # Specifying an occurrence.
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_element(id="heading", occurrence=2, wait=0)
        expected = "Element not found: id=\"heading\", occurrence=2"
        assert str(error.value) == expected

    def test_noninteger_occurrence(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(id="heading", occurrence="abc")
        expected = "The 'occurrence' parameter must be an integer"
        assert str(error.value) == expected

    def test_noninteger_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(id="heading", wait="abc")
        expected = "The 'wait' parameter must be an integer"
        assert str(error.value) == expected

    def test_too_many_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(tag="a", class_name="link")
        expected = (
            "Only one parameter from this list is allowed: class_name, css, "
            "id, link_text, name, partial_link_text, partial_text, tag, text, "
            "type, value, xpath"
        )
        assert str(error.value) == expected

    def test_unrecognised_parameter(self, browser):
        # No recognised parameters, one unrecognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(tag_name=2)
        expected = "These parameters are not recognised: tag_name"
        assert str(error.value) == expected

        # No recognised parameters, multiple unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(bad_parameter=2, other_bad_parameter="abc")
        expected = (
            "These parameters are not recognised: bad_parameter, "
            "other_bad_parameter"
        )
        assert str(error.value) == expected

        # One recognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(tag="a", bad_parameter=2)
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(tag="a", class_name="link", bad_parameter=2)
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised and unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_element(
                tag="a",
                class_name="link",
                bad_parameter=2,
                other_bad_parameter="abc",
            )
        expected = (
            "These parameters are not recognised: bad_parameter, "
            "other_bad_parameter"
        )
        assert str(error.value) == expected
