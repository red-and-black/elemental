=========
Elemental
=========


    Elemental makes Selenium automation faster and easier.


**Adds common use-cases**

Common use-cases missing from Selenium are built into Elemental. *Get an input
by its label or placeholder*? Can do. *Get a button by its text or type?* Sure.
*Get the fourth element in a list?* No problem.

**Automatic waiting**

Elemental has built-in automatic waiting so that your automation is less flaky.
It has a sensible default which can be overriden when necessary.

**The full power of Selenium**

For complex operations which require the full power of the Selenium, Elemental
gives you easy access to 100% of Selenium's API.

**Terse, clean API**

Write less code than you would if you were using Selenium directly. The
Elemental API is terse and internally consistent while still being explicit and
unambiguous.


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


Installation
------------
::

    $ pip install elemental


Development
-----------

Get set up, preferably in a virtualenv::

    $ make init
    $ make install

Lint the code::

    $ make lint

Run the tests::

    $ make test

Build the docs::

    $ cd docs
    $ make html


Releasing
---------

#. Check out the ``main`` branch.

#. Ensure ``CHANGELOG.rst`` includes everything to go in the release and is
   committed.

#. Ensure everything to go in the release is committed.

#. Increment the version in ``elemental/__init__.py`` and
   ``docs/source/conf.py``.

#. Shift everything in the **Unreleased** section of ``CHANGELOG.rst`` to a new
   section named with the new version number and the current date.

#. Ensure CI runs without warnings or errors::

    $ make ci

#. Make and tag the release commit::

    $ make release

#. Build the package::

    $ make package

#. Publish the package to PyPI::

    $ make publish

#. Push to the repo and clean up packaging artifacts::

    $ make push
    $ make clean

#. Create a GitHub release.


Code style
----------

#. Only modules are imported. Classes, functions and variables are not imported
   directly.

#. A module's functions are ordered alphabetically.

#. A module's private functions are placed alphabetically at the bottom of the
   module.

#. Docstrings follow the `NumPy docstring guide
   <https://numpydoc.readthedocs.io/en/latest/format.html>`_.

#. Strings are enclosed with double quotes.

#. The last item of a multi-line dictionary or list has a trailing comma.


Changes
-------

For what has changed in each version, see ``CHANGELOG.rst``.
