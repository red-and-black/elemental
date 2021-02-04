import time

from elemental import exceptions


BUTTON_FINDER_KEYS = [
    "class_name",
    "id",
    "partial_text",
    "text",
    "type",
]


ELEMENT_FINDER_KEYS = [
    "class_name",
    "css",
    "id",
    "link_text",
    "name",
    "partial_link_text",
    "partial_text",
    "tag",
    "text",
    "type",
    "value",
    "xpath",
]


INPUT_FINDER_KEYS = [
    "class_name",
    "id",
    "label",
    "placeholder",
]


def get_button(parent, occurrence=1, wait=5, **kwargs):
    """Get a button from a webpage.

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    occurrence : int, optional
        The occurrence to get. For instance, if multiple buttons on the page
        meet the requirements and the 3rd one is required, set this to 3.
    wait : int, optional
        The time to wait, in seconds, for the button to be found.
    **kwargs
        One and only one keyword argument must be supplied. Allowed keys are:
        "class_name", "id", "partial_text", "text", "type".

    Returns
    -------
    element
        The selected button packaged in an Elemental element.

    Raises
    ------
    NoSuchElementError
        When the button cannot be found.
    ParameterError
        When called with incorrect parameters or parameter values.

    """
    # Validate parameters.
    _validate_kwargs(kwargs, BUTTON_FINDER_KEYS)
    _validate_integer_parameter("occurrence", occurrence, 1)
    _validate_integer_parameter("wait", wait, 0)

    # Get all matching Selenium elements.
    button_kwargs = _build_button_kwargs(parent, kwargs)
    selenium_webelements = _get_selenium_webelements(
        parent,
        button_kwargs,
        occurrence,
        wait,
    )

    # Get the Selenium element if it is in the Selenium elements found or raise
    # an exception.
    if len(selenium_webelements) >= occurrence:
        index = occurrence - 1
        selenium_webelement = selenium_webelements[index]
    else:
        _raise_no_such_element_error("Button", kwargs, occurrence)

    return _create_element(parent, selenium_webelement)


def get_element(parent, occurrence=1, wait=5, **kwargs):
    """Get an element from a webpage.

    This is a wrapper for the family of functions built on Selenium's
    WebDriver.find_element() and WebElement.find_element().

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    occurrence : int, optional
        The occurrence to get. For instance, if multiple elements on the page
        meet the requirements and the 3rd one is required, set this to 3.
    wait : int, optional
        The time to wait, in seconds, for the element to be found.
    **kwargs
        One and only one keyword argument must be supplied. Allowed keys are:
        "class_name", "css", "id", "link_text", "name", "partial_link_text",
        "partial_text", "tag", "text", "type", "value", "xpath".

    Returns
    -------
    element
        The selected HTML element packaged in an Elemental element.

    Raises
    ------
    NoSuchElementError
        When the element cannot be found.
    ParameterError
        When called with incorrect parameters or parameter values.

    """
    # Validate parameters.
    _validate_kwargs(kwargs, ELEMENT_FINDER_KEYS)
    _validate_integer_parameter("occurrence", occurrence, 1)
    _validate_integer_parameter("wait", wait, 0)

    # Get all matching Selenium elements.
    selenium_webelements = _get_selenium_webelements(
        parent,
        kwargs,
        occurrence,
        wait,
    )

    # Get the Selenium element if it is in the Selenium elements found or raise
    # an exception.
    if len(selenium_webelements) >= occurrence:
        index = occurrence - 1
        selenium_webelement = selenium_webelements[index]
    else:
        _raise_no_such_element_error("Element", kwargs, occurrence)

    return _create_element(parent, selenium_webelement)


def get_elements(parent, min_elements=1, wait=5, **kwargs):
    """Get a list of elements from a webpage.

    This is a wrapper for the family of functions built on Selenium's
    WebDriver.find_elements() and WebElement.find_elements().

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    min_elements : int, optional
        The minimum number of elements which must be found to return before the
        wait time expires.
    wait : int, optional
        The time to wait, in seconds, for the elements to be found.
    **kwargs
        One and only one keyword argument must be supplied. Allowed keys are:
        "class_name", "css", "id", "link_text", "name", "partial_link_text",
        "partial_text", "tag", "text", "type", "value", "xpath".

    Returns
    -------
    list of element
        A list of the selected HTML elements, each packaged in an Elemental
        element. An empty list if none are found.

    Raises
    ------
    ParameterError
        When called with incorrect parameters or parameter values.

    """
    # Validate parameters.
    _validate_kwargs(kwargs, ELEMENT_FINDER_KEYS)
    _validate_integer_parameter("min_elements", min_elements, 1)
    _validate_integer_parameter("wait", wait, 0)

    # Get all matching Selenium elements.
    selenium_webelements = _get_selenium_webelements(
        parent,
        kwargs,
        min_elements,
        wait,
    )

    # Create the elements.
    elements = []
    for selenium_webelement in selenium_webelements:
        element = _create_element(parent, selenium_webelement)
        elements.append(element)

    return elements


def get_input(parent, occurrence=1, wait=5, **kwargs):
    """Get an input from a webpage.

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    occurrence : int, optional
        The occurrence to get. For instance, if multiple inputs on the page
        meet the requirements and the 3rd one is required, set this to 3.
    wait : int, optional
        The time to wait, in seconds, for the input to be found.
    **kwargs
        One and only one keyword argument must be supplied. Allowed keys are:
        "class_name", "id", "label", "placeholder".

    Returns
    -------
    element
        The selected input packaged in an Elemental element.

    Raises
    ------
    NoSuchElementError
        When the input cannot be found.
    ParameterError
        When called with incorrect parameters or parameter values.

    """
    # Validate parameters.
    _validate_kwargs(kwargs, INPUT_FINDER_KEYS)
    _validate_integer_parameter("occurrence", occurrence, 1)
    _validate_integer_parameter("wait", wait, 0)

    # Get all matching Selenium elements.
    input_kwargs = _build_input_kwargs(parent, kwargs)
    selenium_webelements = _get_selenium_webelements(
        parent,
        input_kwargs,
        occurrence,
        wait,
    )

    # Get the Selenium element if it is in the Selenium elements found or raise
    # an exception.
    if len(selenium_webelements) >= occurrence:
        index = occurrence - 1
        selenium_webelement = selenium_webelements[index]
    else:
        _raise_no_such_element_error("Input", kwargs, occurrence)

    # If the finder type is 'label', selenium_webelement corresponds to a label
    # for which the matching input must be found.
    finder_type, _ = list(kwargs.items())[0]
    if finder_type == "label":
        input_id = selenium_webelement.get_attribute("for")
        try:
            input_element = parent.get_element(id=input_id, wait=0)
        except exceptions.NoSuchElementError:
            _raise_no_such_element_error("Input", kwargs, occurrence)
        selenium_webelement = input_element.selenium_webelement

    return _create_element(parent, selenium_webelement)


def _build_button_kwargs(parent, kwargs):
    """Make an dictionary containing an xpath expression to find a button.

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    kwargs : dict
        Keyword arguments.

    Returns
    -------
    dict
        A dict in the form {"xpath": <xpath_expression>}.

    """
    prefix = _build_xpath_prefix(parent)
    finder_type, finder_value = list(kwargs.items())[0]
    sanitised_finder_value = _sanitise_finder_value_for_xpath(finder_value)

    if finder_type == "class_name":
        xpath = "{}button[@class={}]".format(prefix, sanitised_finder_value)
    elif finder_type == "id":
        xpath = "{}button[@id={}]".format(prefix, sanitised_finder_value)
    elif finder_type == "partial_text":
        xpath = (
            "{}button[contains(string(), {})]"
            .format(prefix, sanitised_finder_value)
        )
    elif finder_type == "text":
        xpath = (
            "{}button[normalize-space(string())={}]"
            .format(prefix, sanitised_finder_value)
        )
    elif finder_type == "type":
        xpath = "{}button[@type={}]".format(prefix, sanitised_finder_value)

    return {"xpath": xpath}


def _build_input_kwargs(parent, kwargs):
    """Make an dictionary containing an xpath expression to find an input.

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    kwargs
        Keyword arguments.

    Returns
    -------
    dict
        A dict in the form {"xpath": <xpath_expression>}.

    """
    prefix = _build_xpath_prefix(parent)
    finder_type, finder_value = list(kwargs.items())[0]
    sanitised_finder_value = _sanitise_finder_value_for_xpath(finder_value)

    if finder_type == "class_name":
        xpath = "{}input[@class={}]".format(prefix, sanitised_finder_value)
    elif finder_type == "id":
        xpath = "{}input[@id={}]".format(prefix, sanitised_finder_value)
    elif finder_type == "label":
        xpath = (
            "{}label[normalize-space(string())={}]"
            .format(prefix, sanitised_finder_value)
        )
    elif finder_type == "placeholder":
        xpath = (
            "{}input[@placeholder={}]".format(prefix, sanitised_finder_value)
        )

    return {"xpath": xpath}


def _build_xpath_prefix(parent):
    """Make the prefix for an xpath expression.

    The prefix of an xpath expression determines whether it operates relative
    to an element ("descendant::") or the document root ("//").

    Parameters
    ----------
    parent : browser or element
        The browser or element.

    Returns
    -------
    Str
        Either "descendant::" or "//".

    """
    return "descendant::" if isinstance(parent, parent.element_class) else "//"


def _create_element(parent, selenium_webelement):
    """Create an element from a Selenium webelement.

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    selenium_webelement : Selenium webelement
        The Selenium webelement.

    Returns
    -------
    element
        The element.

    """
    element_class = parent.element_class
    selenium_webdriver = parent.selenium_webdriver
    return element_class(selenium_webdriver, selenium_webelement)


def _find_with_selenium(parent, finder_type, finder_value):
    """Find Selenium webelements.

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    finder_type : str
        One of the ELEMENT_FINDER_KEYS.
    finder_value: str
        The value to match elements on.

    Returns
    -------
    list of webelement
        A list of Selenium webelements. An empty list if none are found.

    """
    # Handle the 'partial_text' and 'text' finder types using xpaths, as they
    # are not built in to Selenium. The xpath expressions ignore the contents
    # of script tags so as to not pick up false positives from JavaScript code.
    if finder_type in ["partial_text", "text", "type", "value"]:
        prefix = _build_xpath_prefix(parent)
        sanitised_finder_value = _sanitise_finder_value_for_xpath(finder_value)
        if finder_type == "partial_text":
            finder_value = (
                "{}*[contains(text(), {})][not(self::script)]"
                .format(prefix, sanitised_finder_value)
            )
        elif finder_type == "text":
            finder_value = (
                "{}*[normalize-space(text())={}][not(self::script)]"
                .format(prefix, sanitised_finder_value)
            )
        elif finder_type == "type":
            finder_value = (
                "{}*[@type={}]".format(prefix, sanitised_finder_value)
            )
        elif finder_type == "value":
            finder_value = (
                "{}*[@value={}]".format(prefix, sanitised_finder_value)
            )
        selenium_find_by = "xpath"

    # Translate the 'css' finder type to its Selenium equivalent.
    elif finder_type == "css":
        selenium_find_by = "css selector"
    # Translate the 'tag' finder type to its Selenium equivalent.
    elif finder_type == "tag":
        selenium_find_by = "tag name"
    # Translate any other finder type to its Selenium equivalent.
    else:
        selenium_find_by = finder_type.replace("_", " ")

    selenium_parent = _get_selenium_parent(parent)

    return selenium_parent.find_elements(selenium_find_by, finder_value)


def _get_selenium_webelements(parent, kwargs, min_elements, wait):
    """Get all Selenium elements matching the kwargs.

    Parameters
    ----------
    parent : browser or element
        The browser or element.
    kwargs : dict
        Keyword arguments.
    min_elements : int, optional
        The minimum number of elements which must be found to return before the
        wait time expires.
    wait : int, optional
        The time to wait, in seconds, for the elements to be found.

    Returns
    -------
    list of webelement
        A list of Selenium webelements. An empty list if none are found.

    """
    # Prepare to find the matching Selenium elements.
    finder_type, finder_value = list(kwargs.items())[0]

    # Wait until either enough matching Selenium elements are found or the wait
    # time runs out.
    end_time = time.time() + wait
    selenium_webelements = _find_with_selenium(
        parent,
        finder_type,
        finder_value,
    )
    while len(selenium_webelements) < min_elements and end_time > time.time():
        selenium_webelements = _find_with_selenium(
            parent,
            finder_type,
            finder_value,
        )

    return selenium_webelements


def _get_selenium_parent(parent):
    """Supply the Selenium webdriver or webelement.

    Parameters
    ----------
    parent : browser or element
        The browser or element.

    Returns
    -------
    Selenium webdriver or Selenium webelement
        If parent is a browser, the Selenium webdriver.
        If parent is an element, the Selenium webelement.

    """
    if isinstance(parent, parent.element_class):
        return parent.selenium_webelement
    return parent.selenium_webdriver


def _raise_no_such_element_error(element_type, kwargs, occurrence):
    """Raise a NoSuchElementError.

    Parameters
    ----------
    element_type : str
        The type of element which was being searched for. For example:
        "Button".
    kwargs : dict
        Keyword arguments used to search.
    occurrence : int
        The element occurrence which was being searched for.

    Returns
    -------
    None

    Raises
    ------
    NoSuchElementError

    """
    finder_type, finder_value = list(kwargs.items())[0]
    error = (
        "{} not found: {}=\"{}\""
        .format(element_type, finder_type, finder_value)
    )
    if occurrence != 1:
        error = "{}, occurrence={}".format(error, occurrence)

    raise exceptions.NoSuchElementError(error)


def _sanitise_finder_value_for_xpath(finder_value):
    r"""Handle single quotes in finder values before using them with xpath.

    Parameters
    ----------
    finder_value : str
        A string.

    Returns
    -------
    str
        The string formatted as a an xpath concat function if it contains one
        or more single quotes, otherwise the original string wrapped in single
        quotes.

    Examples
    --------
    >>> _sanitise_finder_value_for_xpath("What's happening here?")
    'concat(\'What\', "\'", \'s happening here?\')'
    >>> _sanitise_finder_value_for_xpath("hello")
    "'hello'"

    """
    if "'" not in finder_value:
        return "'{}'".format(finder_value)

    value_with_single_quotes_quoted = finder_value.replace("'", "', \"'\", '")
    return "concat('{}')".format(value_with_single_quotes_quoted)


def _validate_integer_parameter(name, value, min_value):
    """Validate a parameter which receives an integer.

    Parameters
    ----------
    name: str
        The name of the parameter.
    value : int
        The value supplied to the parameter.
    min_value : int
        The minimum allowable value of the parameter.

    Raises
    ------
    ParameterError
        For bad values of the parameter.

    """
    if not isinstance(value, int):
        raise exceptions.ParameterError(
            "The '{}' parameter must be an integer".format(name),
        )
    if value < min_value:
        raise exceptions.ParameterError(
            "The '{}' parameter cannot be less than {}"
            .format(name, min_value),
        )


def _validate_kwargs(kwargs, finder_keys):
    """Validate the kwargs.

    Parameters
    ----------
    kwargs : dict
        Keyword arguments.
    finder_keys : list of str
        Allowed keyword argument keys.

    Raises
    ------
    ParameterError
        When there are too many kwargs, or unrecognised or bad kwargs.

    """
    unrecognised_keys = [key for key in kwargs if key not in finder_keys]
    if unrecognised_keys:
        raise exceptions.ParameterError(
            "These parameters are not recognised: {}"
            .format(", ".join(sorted(unrecognised_keys))),
        )
    if len(kwargs) == 0:
        raise exceptions.ParameterError(
            "One parameter from this list is required: {}"
            .format(", ".join(sorted(finder_keys))),
        )
    if len(kwargs) > 1:
        raise exceptions.ParameterError(
            "Only one parameter from this list is allowed: {}"
            .format(", ".join(sorted(finder_keys))),
        )
