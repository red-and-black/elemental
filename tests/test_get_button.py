import pytest

from elemental import exceptions
from tests import utilities


@pytest.fixture
def test_getters_page(browser):
    url = utilities.build_url("test_getters.html")
    browser.selenium_webdriver.get(url)


@pytest.mark.usefixtures("test_getters_page")
class TestGetButton:

    def test_by_class_name(self, browser):
        element = browser.get_button(class_name="primary")
        assert element.selenium_webelement.text == "Add paragraph"

    def test_by_id(self, browser):
        element = browser.get_button(id="add-button")
        assert element.selenium_webelement.text == "Add paragraph"

    def test_by_partial_text(self, browser):
        element = browser.get_button(partial_text="I'm a paragraph add")
        assert element.selenium_webelement.text == "I'm a paragraph adder"

    def test_by_text(self, browser):
        element = browser.get_button(text="I'm a paragraph adder")
        assert element.selenium_webelement.text == "I'm a paragraph adder"

    def test_by_type(self, browser):
        element = browser.get_button(type="button")
        assert element.selenium_webelement.text == "Add paragraph"

    def test_chaining(self, browser):
        # Ensure that the button is found by partial_text from the element and
        # not the page root.
        element = browser.\
            get_element(class_name="container", occurrence=5).\
            get_button(partial_text="paragraph")
        assert element.selenium_webelement.text == "I'm a paragraph adder"

        # Ensure that the button is found by text from the element and not the
        # page root.
        element = browser.\
            get_element(class_name="container", occurrence=5).\
            get_button(text="I'm a paragraph adder")
        assert element.selenium_webelement.text == "I'm a paragraph adder"

    def test_no_waiting(self, browser):
        element = browser.get_button(id="add-button", wait=0)
        assert element.selenium_webelement.text == "Add paragraph"

    def test_occurrence(self, browser):
        element = browser.get_button(partial_text="para", occurrence=2)
        assert element.selenium_webelement.text == "I'm a paragraph adder"


@pytest.mark.usefixtures("test_getters_page")
class TestGetButtonErrors:

    def test_forbidden_occurrence(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(id="add-button", occurrence=0)
        expected = "The 'occurrence' parameter cannot be less than 1"
        assert str(error.value) == expected

    def test_forbidden_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(id="add-button", wait=-2)
        expected = "The 'wait' parameter cannot be less than 0"
        assert str(error.value) == expected

    def test_insufficient_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button()
        expected = (
            "One parameter from this list is required: class_name, id, "
            "partial_text, text, type"
        )
        assert str(error.value) == expected

    def test_nonbutton_element(self, browser):
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_button(id="para-2", wait=0)
        expected = "Button not found: id=\"para-2\""
        assert str(error.value) == expected

    def test_nonexistent_element(self, browser):
        # Without specifying the occurrence.
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_button(id="abc", wait=0)
        expected = "Button not found: id=\"abc\""
        assert str(error.value) == expected

        # Specifying an occurrence.
        with pytest.raises(exceptions.NoSuchElementError) as error:
            browser.get_button(id="add-button", occurrence=2, wait=0)
        expected = "Button not found: id=\"add-button\", occurrence=2"
        assert str(error.value) == expected

    def test_noninteger_occurrence(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(id="add-button", occurrence="abc")
        expected = "The 'occurrence' parameter must be an integer"
        assert str(error.value) == expected

    def test_noninteger_wait(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(id="add-button", wait="abc")
        expected = "The 'wait' parameter must be an integer"
        assert str(error.value) == expected

    def test_too_many_parameters(self, browser):
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(class_name="primary", id="add-button")
        expected = (
            "Only one parameter from this list is allowed: class_name, id, "
            "partial_text, text, type"
        )
        assert str(error.value) == expected

    def test_unrecognised_parameter(self, browser):
        # No recognised parameters, one unrecognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(tag_name=2)
        expected = "These parameters are not recognised: tag_name"
        assert str(error.value) == expected

        # No recognised parameters, multiple unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(bad_parameter=2, other_bad_parameter="abc")
        expected = (
            "These parameters are not recognised: bad_parameter, "
            "other_bad_parameter"
        )
        assert str(error.value) == expected

        # One recognised parameter.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(type="button", bad_parameter=2)
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(
                class_name="primary",
                type="button",
                bad_parameter=2,
            )
        expected = "These parameters are not recognised: bad_parameter"
        assert str(error.value) == expected

        # Multiple recognised and unrecognised parameters.
        with pytest.raises(exceptions.ParameterError) as error:
            browser.get_button(
                class_name="primary",
                type="button",
                bad_parameter=2,
                other_bad_parameter="abc",
            )
        expected = (
            "These parameters are not recognised: bad_parameter, "
            "other_bad_parameter"
        )
        assert str(error.value) == expected
