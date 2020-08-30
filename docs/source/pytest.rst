Pytest + Elemental
==================


Step 1. Create the browser fixture
----------------------------------

Add the ``browser`` session-scoped fixture to Pytest's ``conftest.py`` file.


.. code:: python

   # tests/conftest.py
   import elemental
   import pytest

   @pytest.fixture(scope="session")
   def browser():
       # Create and yield the browser.
       _browser = elemental.Browser(headless=True)
        yield _browser

        # Stop the browser after the tests have finished.
        _browser.quit()


Step 2. Use the fixture
-----------------------

Then use it in your test files.


.. code:: python

   # tests/test_navigation.py
   def test_pypi(browser):
       browser.visit("https://pypi.org")
       assert browser.title == "PyPI · The Python Package Index"
