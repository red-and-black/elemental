Getters
=======
Getters get an element.

They operate on an element or browser and return an element or list of elements.

Getters can be chained (see :ref:`chaining_getters`).


get_button
----------

.. function::
   get_button(occurrence=1, wait=5, **kwargs)

Gets a button by class, id, partial text, text or type.

*Parameters*
  :occurrence:
    :class:`int, optional` The occurrence to get. For instance, if multiple
    buttons on the page meet the requirements and the 3rd one is required, set
    this to 3.

  :wait:
    :class:`int, optional` The time to wait, in seconds, for the button to be found.

  :kwargs:
    One and only one keyword argument must be supplied. Allowed keys are:
    "class_name", "id", "partial_text", "text", "type".

*Returns*
  :class:`element`

*Examples*
  .. code-block:: python

     >>> browser.get_button(class_name="primary")
     >>> browser.get_button(id="my-button")
     >>> browser.get_button(partial_text="Save document")
     >>> browser.get_button(text="Save document now", wait=30)
     >>> browser.get_button(type="submit")


get_element
-----------

.. function::
  get_element(occurrence=1, wait=5, **kwargs)

Gets any element.

*Parameters*
  :occurrence:
    :class:`int, optional` The occurrence to get. For instance, if multiple
    links on the page meet the requirements and the 3rd one is required, set
    this to 3.

  :wait:
    :class:`int, optional` The time to wait, in seconds, for the element to
    be found.

  :kwargs:
    One and only one keyword argument must be supplied. Allowed keys are:
    "class_name", "css", "id", "link_text", "name", "partial_link_text",
    "partial_text", "tag", "text", "type", "xpath".

*Returns*
  :class:`element`

*Examples*
  .. code-block:: python

     >>> browser.get_element(class_name="link")
     >>> browser.get_element(css="div.container p", wait=10)
     >>> browser.get_element(id="heading")
     >>> browser.get_element(link_text="Python Package Index (PyPI)")
     >>> browser.get_element(name="para-1")
     >>> browser.get_element(partial_link_text="PyPI")
     >>> browser.get_element(partial_text="Paragraph", occurrence=2)
     >>> browser.get_element(tag="a")
     >>> browser.get_element(text="Some text")
     >>> browser.get_element(type="button")
     >>> browser.get_element(xpath="//*[@id='para-2']")
     >>> browser.get_element(tag="div").get_element(id="primary")


get_elements
------------

.. function::
   get_elements(min_elements=1, wait=5, **kwargs)

Gets a list of elements.

*Parameters*
  :min_elements:
    :class:`int, optional` The minimum number of elements which must be found
    to return before the wait time expires.

  :wait:
    :class:`int, optional` The time to wait, in seconds, for the elements
    to be found.

  :kwargs:
    One and only one keyword argument must be supplied. Allowed keys are:
    "class_name", "css", "id", "link_text", "name", "partial_link_text",
    "partial_text", "tag", "text", "type", "xpath".

*Returns*
  :class:`list of elements`

*Examples*
  .. code-block:: python

     >>> browser.get_elements(class_name="link")
     >>> browser.get_elements(css="div.container a")
     >>> browser.get_elements(id="heading")
     >>> browser.get_elements(link_text="Python.org")
     >>> browser.get_elements(name="para-1")
     >>> browser.get_elements(partial_link_text="Python")
     >>> browser.get_elements(partial_text="Paragraph")
     >>> browser.get_elements(tag="p", min_elements=5, wait=0)
     >>> browser.get_elements(text="Python.org")
     >>> browser.get_elements(type="button")
     >>> browser.get_elements(xpath="//*[@class='para']")
     >>> browser.get_element(class_name="container").get_elements(tag="p")


get_input
---------

.. function::
   get_input(occurrence=1, wait=5, **kwargs)

Gets an input field by class, id, label, or placeholder text.

*Parameters*
  :occurrence:
    :class:`int, optional` The occurrence to get. For instance, if multiple
    inputs on the page meet the requirements and the 3rd one is required, set
    this to 3.

  :wait:
    :class:`int, optional` The time to wait, in seconds, for the input field
    to be found.

  :kwargs::
    One and only one keyword argument must be supplied. Allowed keys are:
    "class_name", "id", "label", "placeholder".

*Returns*
  :class:`element`

*Examples*
  .. code-block:: python

     >>> browser.get_input(class_name="input", wait=0, occurrence=2)
     >>> browser.get_input(id="full-name")
     >>> browser.get_input(label="Full name")
     >>> browser.get_input(placeholder="Enter your full name")


.. _chaining_getters:

Chaining getters
----------------

You can chain getters together to zero in on the element or list of elements
you want. Note you cannot chain another getter after `get_elements`.

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="my-form").get_button(type="submit")
     >>> browser.get_element(tag="div").get_element(id="primary")
     >>> browser.get_element(class_name="container").get_elements(tag="p")
     >>> browser.get_element(tag="form").get_input(label="Full name")
