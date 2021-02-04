import pytest

from elemental import exceptions
from tests import utilities


@pytest.fixture
def test_getters_page(browser):
    url = utilities.build_url("test_getters.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_getters_page")
class TestGetInput:

    def test_by_class_name(self, browser):
        element = browser.get_input(class_name="input")
        actual = element.selenium_webelement.get_attribute("placeholder")
        assert actual == "I'm Placeholder 1"

    def test_by_id(self, browser):
        element = browser.get_input(id="input-2")
        actual = element.selenium_webelement.get_attribute("placeholder")
        assert actual == "Placeholder 2"

    def test_by_label(self, browser):
        # Test without quotes.
        element = browser.get_input(label="Input 1")
        actual = element.selenium_webelement.get_attribute("placeholder")
        assert actual == "I'm Placeholder 1"

        # Test with single and double quotes.
        element = browser.get_input(label="I've read the \"T's & C's\"")
        actual = element.selenium_webelement.get_attribute("id")
        assert actual == "input-4"

        # Test for an input which is not an immediate child.
        container = browser.get_element(class_name="container", occurrence=4)
        element = container.get_input(label="Nested checkbox")
        actual = element.selenium_webelement.get_attribute("id")
        assert actual == "input-5"

        # Test for a label containing a nested element.
        element = browser.get_input(
            label="Checkbox with nested element in label",
        )
        actual = element.selenium_webelement.get_attribute("id")
        assert actual == "input-6"

    def test_by_placeholder(self, browser):
        element = browser.get_input(placeholder="I'm Placeholder 1")
        actual = element.selenium_webelement.get_attribute("placeholder")
        assert actual == "I'm Placeholder 1"

    def test_chaining(self, browser):
        # Ensure that the input is found from the element and not the page
        # root.
        element = browser.\
            get_element(class_name="container", occurrence=3).\
            get_input(label="Input 2")
        actual = element.selenium_webelement.get_attribute("placeholder")
        assert actual == "Placeholder 2"

    def test_no_waiting(self, browser):
        element = browser.get_input(id="input-1", wait=0)
        actual = element.selenium_webelement.get_attribute("placeholder")
        assert actual == "I'm Placeholder 1"

    def test_occurrence(self, browser):
        element = browser.get_input(class_name="input", occurrence=2)
        actual = element.selenium_webelement.get_attribute("placeholder")
        assert actual == "Placeholder 2"


@pytest.mark.usefixtures("test_getters_page")
class TestGetInputErrors:

    def test_forbidden_occurrence(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(id="input-1", occurrence=0)
        expected = "The 'occurrence' parameter cannot be less than 1"
        assert str(error.value) == expected

    def test_forbidden_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(id="input-1", wait=-2)
        expected = "The 'wait' parameter cannot be less than 0"
        assert str(error.value) == expected

    def test_insufficient_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input()
        expected = (
            "One parameter from this list is required: class_name, id, label, "
            "placeholder"
        )
        assert str(error.value) == expected

    def test_label_without_input(self, browser):
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_input(label="Label with no input", wait=0)
        expected = "Input not found: label=\"Label with no input\""
        assert str(error.value) == expected

    def test_noninput_element(self, browser):
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_input(id="input-3", wait=0)
        expected = "Input not found: id=\"input-3\""
        assert str(error.value) == expected

    def test_nonexistent_element(self, browser):
        # Without specifying the occurrence.
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_input(id="abc", wait=0)
        expected = "Input not found: id=\"abc\""
        assert str(error.value) == expected

        # Specifying an occurrence.
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_input(id="input-1", occurrence=2, wait=0)
        expected = "Input not found: id=\"input-1\", occurrence=2"
        assert str(error.value) == expected

    def test_noninteger_occurrence(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(id="input-1", occurrence="abc")
        expected = "The 'occurrence' parameter must be an integer"
        assert str(error.value) == expected

    def test_noninteger_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(id="input-1", wait="abc")
        expected = "The 'wait' parameter must be an integer"
        assert str(error.value) == expected

    def test_too_many_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(class_name="primary", id="input-1")
        expected = (
            "Only one parameter from this list is allowed: class_name, id, "
            "label, placeholder"
        )
        assert str(error.value) == expected

    def test_unrecognised_parameter(self, browser):
        # No recognised parameters, one unrecognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(tag_name=2)
        expected = "These parameters are not recognised: tag_name"
        assert str(error.value) == expected

        # No recognised parameters, multiple unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(bad_parameter=2, other_bad_parameter="abc")
        expected = (
            "These parameters are not recognised: bad_parameter, "
            "other_bad_parameter"
        )
        assert str(error.value) == expected

        # One recognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(class_name="input", bad_parameter=2)
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(
                class_name="primary",
                id="input-2",
                bad_parameter=2,
            )
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised and unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_input(
                class_name="primary",
                id="input-2",
                bad_parameter=2,
                other_bad_parameter="abc",
            )
        expected = (
            "These parameters are not recognised: bad_parameter, "
            "other_bad_parameter"
        )
        assert str(error.value) == expected
