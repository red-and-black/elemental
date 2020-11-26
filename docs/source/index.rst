Elemental
=========


Elemental makes Selenium automation faster and easier.


Adds common use-cases
    Common use-cases missing from Selenium are built into Elemental. *Get an
    input by its label or placeholder*? Can do. *Get a button by its text or
    type?* Sure. *Get an element's parent?* Yep. *Get the fourth element in a
    list?* No problem.

Automatic waiting
    Elemental has built-in automatic waiting so that your automation is less
    flaky. It has a sensible default which can be overriden when necessary.

The full power of Selenium
    For complex operations which require the full power of the Selenium,
    Elemental gives you easy access to 100% of Selenium's API.

Terse, clean API
    Write less code than you would if you were using Selenium directly. The
    Elemental API is terse and internally consistent while still being explicit
    and unambiguous.


The power of Elemental
----------------------

.. code:: python

    import elemental

    # Set up.
    browser = elemental.Browser()

    # Search PyPI for Elemental.
    browser.visit("https://www.pypi.org")
    browser.get_input(placeholder="Search projects").fill("elemental")
    browser.get_button(type="submit").click()

    # Click the first search result.
    browser.get_element(partial_text="elemental").click()

    # Confirm that Elemental's PyPI page was found.
    assert browser.title == "elemental · PyPI"

    # Tear down.
    browser.quit()


.. admonition:: Now dig in

   Check out :doc:`Elemental's functionality </functionality>` or
   :doc:`install it now </first_steps>` and make working with Selenium faster and
   easier.


.. toctree::
   :caption: GETTING STARTED
   :hidden:

   functionality
   first_steps

.. toctree::
   :caption: TUTORIALS
   :hidden:

   behave
   pytest

.. toctree::
   :caption: REFERENCE
   :hidden:

   actions
   getters
   states
   values

   browser
   raw_selenium

.. toctree::
   :caption: CONTRIBUTING
   :hidden:

   contributions
   source
