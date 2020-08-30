=========
Elemental
=========

    Faster, easier and more robust Selenium automation.


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


Releasing
---------

#. Check out the ``master`` branch.

#. Ensure ``CHANGELOG.rst`` includes everything to go in the release and is
   committed.

#. Ensure everything to go in the release is committed.

#. Increment the version in ``__init__.py``.

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
