Actions
=======

Action functions cause the driver to complete an action, either on an element
or the browser.

These functions operate on an element or browser, and don't return.


check
-----
.. function::
  check()

Checks a checkbox. Always leaves the checkbox in a 'selected' state, no matter
whether it was checked or unchecked when the action was performed.

*Returns*
  :class:`None`

*Example*
  .. code-block:: python

     >>> browser.get_element(id="my_checkbox").check()


click
-----
.. function::
 click()

Clicks the element.

*Returns*
 :class:`None`

*Examples*
 .. code-block:: python

    >>> browser.get_button(id="my-button").click()
    >>> browser.get_element(link_text="Python Package Index (PyPI)").click()


fill
----
.. function::
  fill(string)

Fills an input field with a string of text or filepath. Clears any existing
input from the field prior to filling.

*Parameters*
  :string:
    :class:`str` The text or filepath as a string.

*Returns*
  :class:`None`

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="my_input_field").fill("my_string")
     >>> browser.get_input(label="Attach file").fill("my_filepath")


quit
----
.. function::
  quit()

Quits the browser. Operates on a browser, not an element.

*Returns*
  :class:`None`

*Example*
  .. code-block:: python

     >>> browser.quit()


screenshot
----------
.. function::
  screenshot(filepath)

Takes a screenshot of either the full browser or an element, and saves it
to a given filepath.

*Parameters*
  :filepath:
    :class:`str` The full filepath, as a string.

*Returns*
  :class:`None`

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="screenshot").screenshot("element.png")
     >>> browser.screenshot("page.png")


select
------
.. function::
  select()

Selects a radio button, select option, or checkbox element. Always leaves the
target element in a selected state, no matter whether it was already selected.

*Returns*
  :class:`None`

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="my_radio_button").select()
     >>> browser.get_element(id="selector_id").get_element(text="option_text").select()
     >>> browser.get_element(id="selector_id").get_element(value="option_value").select()


uncheck
-------
.. function::
  uncheck()

Unchecks a checkbox. Always leaves the checkbox in a 'not selected' state, no
matter whether it was checked or unchecked when the action was performed.

*Returns*
  :class:`None`

*Example*
  .. code-block:: python

     >>> browser.get_element(id="my_checkbox").uncheck()


visit
-----
.. function::
  visit(url)

Visits a url in the browser.

*Parameters*
  :url:
    :class:`str` The URL as a string.

*Returns*
  :class:`None`

*Example*
  .. code-block:: python

     >>> browser.visit("https://redandblack.io")
