import pytest

from elemental import exceptions
from tests import utilities


@pytest.fixture
def test_getters_page(browser):
    url = utilities.build_url("test_getters.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_getters_page")
class TestGetElements:

    def test_by_class_name(self, browser):
        elements = browser.get_elements(class_name="link")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Python Package Index (PyPI)", "Python.org"]

    def test_by_css(self, browser):
        elements = browser.get_elements(css="div.container a")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Python Package Index (PyPI)", "Python.org"]

    def test_by_id(self, browser):
        elements = browser.get_elements(id="heading")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Heading"]

    def test_by_link_text(self, browser):
        elements = browser.get_elements(link_text="Python.org")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Python.org"]

    def test_by_name(self, browser):
        elements = browser.get_elements(name="para-1")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 1"]

    def test_by_partial_link_text(self, browser):
        elements = browser.get_elements(partial_link_text="Python")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Python Package Index (PyPI)", "Python.org"]

    def test_by_partial_text(self, browser):
        elements = browser.get_elements(partial_text="Paragraph")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 1", "Paragraph 2", "Paragraph 3"]

    def test_by_tag(self, browser):
        elements = browser.get_elements(tag="p")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 1", "Paragraph 2", "Paragraph 3"]

    def test_by_text(self, browser):
        elements = browser.get_elements(text="Python.org")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Python.org"]

    def test_by_type(self, browser):
        elements = browser.get_elements(type="button")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Add paragraph", "Add paragraph (secondary)"]

    def test_by_xpath(self, browser):
        elements = browser.get_elements(xpath="//*[@class='para']")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 1", "Paragraph 2", "Paragraph 3"]

    def test_chaining(self, browser):
        # Ensure that 'partial_text' finds from the element and not the page
        # root.
        elements = browser.\
            get_element(class_name="container").\
            get_elements(partial_text="Paragraph")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 3"]

        # Ensure that 'text' finds from the element and not the page root.
        elements = browser.\
            get_element(class_name="container").\
            get_elements(text="Paragraph 3")
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 3"]

    def test_large_min_elements(self, browser):
        elements = browser.get_elements(tag="p", min_elements=5, wait=0)
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 1", "Paragraph 2", "Paragraph 3"]

    def test_min_elements(self, browser):
        elements = browser.get_elements(tag="p", min_elements=3)
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Paragraph 1", "Paragraph 2", "Paragraph 3"]

    def test_min_elements_with_wait(self, browser):
        browser.selenium_webdriver.find_element_by_tag_name("button").click()
        elements = browser.get_elements(tag="p", min_elements=4)
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == [
            "Paragraph 1",
            "Paragraph 2",
            "Paragraph 3",
            "Paragraph 4",
        ]

    def test_no_waiting(self, browser):
        elements = browser.get_elements(id="heading", wait=0)
        contents = [element.selenium_webelement.text for element in elements]
        assert contents == ["Heading"]

    def test_nonexistent_elements(self, browser):
        # Without specifying minimum elements.
        elements = browser.get_elements(id="abc", wait=0)
        assert elements == []

        # Specifying minimum elements.
        elements = browser.get_elements(id="abc", min_elements=2, wait=0)
        assert elements == []


@pytest.mark.usefixtures("test_getters_page")
class TestGetElementsErrors:

    def test_forbidden_min_elements(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(id="heading", min_elements=0)
        expected = "The 'min_elements' parameter cannot be less than 1"
        assert str(error.value) == expected

    def test_forbidden_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(id="heading", wait=-2)
        expected = "The 'wait' parameter cannot be less than 0"
        assert str(error.value) == expected

    def test_insufficient_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements()
        expected = (
            "One parameter from this list is required: class_name, css, id, "
            "link_text, name, partial_link_text, partial_text, tag, text, "
            "type, xpath"
        )
        assert str(error.value) == expected

    def test_noninteger_min_elements(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(id="heading", min_elements="abc")
        expected = "The 'min_elements' parameter must be an integer"
        assert str(error.value) == expected

    def test_noninteger_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(id="heading", wait="abc")
        expected = "The 'wait' parameter must be an integer"
        assert str(error.value) == expected

    def test_too_many_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(tag="a", class_name="link")
        expected = (
            "Only one parameter from this list is allowed: class_name, css, "
            "id, link_text, name, partial_link_text, partial_text, tag, text, "
            "type, xpath"
        )
        assert str(error.value) == expected

    def test_unrecognised_parameter(self, browser):
        # No recognised parameters, one unrecognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(tag_name="p")
        expected = "These parameters are not recognised: tag_name"
        assert str(error.value) == expected

        # No recognised parameters, multiple unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(bad_parameter=2, other_bad_parameter="abc")
        expected = (
            "These parameters are not recognised: bad_parameter, "
            "other_bad_parameter"
        )
        assert str(error.value) == expected

        # One recognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(tag="a", bad_parameter=2)
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(tag="a", class_name="link", bad_parameter=2)
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised and unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_elements(
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
