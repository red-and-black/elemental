Values
======
Values functions get the value of an element, or one of it's attributes.

These functions operate on an element or browser, and return a string or
boolean.


attribute
---------
.. attribute::
  attribute(attribute_name)

Gets the value of an attribute.

*Parameters*
  :attribute_name:
    :class:`str` The name of the attribute. For instance, "hidden", or "class".

*Returns*
  :class:`str` or :class:`bool` For boolean attributes like "hidden" a boolean
  is returned. For other attributes a string is returned.

*Examples*
  .. code-block:: python

     >>> browser.get_element(id="hiding").attribute("hidden")
     True
     >>> browser.get_element(id="my_id").attribute("id")
     "my_id"


html
-----
.. attribute::
  html

Gets the html for an element or whole page.

*Returns*
  :class:`str` The html for the element or page, as a string.

*Example*
  .. code-block:: python

     >>> browser.get_element(tag="p").html
     "<p>This is a paragraph.</p>"


text
----
.. attribute::
  text

Gets the text of an element.

*Returns*
  :class:`str` The text of the element, as a string.

*Example*
  .. code-block:: python

     >>> browser.get_element(tag="p").text
     "This is some text"


title
-----
.. attribute::
  title

Gets the title of a page.

*Returns*
  :class:`str` The text of the page title, as a string.

*Example*
  .. code-block:: python

     >>> browser.title
     "A Page Title"


url
---
.. attribute::
  url

Gets the url of a page.

*Returns*
  :class:`str` The url of the current page, as a string.

*Example*
  .. code-block:: python

     >>> browser.url
     "https://redandblack.io"
