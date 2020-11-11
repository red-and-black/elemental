States
======

States functions are used to determine whether an element has a state, such
as whether it is displayed or selected.

These functions operate on an element, and return a boolean.


is_displayed
------------
.. attribute::
  is_displayed

Determines whether an element is displayed to the user.

*Returns*
  :class:`bool` True if displayed, False otherwise.

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="not-hiding").is_displayed
     True
     >>> browser.get_element(id="hiding").is_displayed
     False

.. note::

   ``is_displayed`` does not work on hidden select options.



is_enabled
----------
.. attribute::
  is_enabled

Determines whether an element is enabled or disabled.

*Returns*
  :class:`bool` True if enabled, False otherwise.

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="available").is_enabled
     True
     >>> browser.get_element(id="disabled").is_enabled
     False


is_selected
-----------
.. attribute::
  is_selected

Determines whether a radio button, checkbox or select option is selected.

*Returns*
  :class:`bool` True if selected, False otherwise.

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="checked").is_selected
     True
     >>> browser.get_element(id="unchecked").is_selected
     False
