Behave + Elemental
==================


Step 1. Create the browser fixture
----------------------------------

Add the ``browser`` fixture to Behave's ``environment.py`` file.

.. code:: python

   # features/environment.py
   from behave import (
       fixture,
       use_fixture,
   )
   import elemental

   @fixture
   def browser(context):
       # Create and yield the browser.
       context.browser = elemental.Browser(headless=True)
       yield context.browser

        # Stop the browser after the tests have finished.
       context.browser.quit()

   def before_all(context):
       use_fixture(browser, context)


Step 2. Use the fixture
-----------------------

Then use it in your step implementation files.


.. code:: python

   # features/steps/navigation.py
   from behave import (
       when,
       then,
    )

   @when("I browse to PyPI")
   def step_impl(context):
       context.browser.visit("https://pypi.org")

   @then("I see PyPI's title")
   def step_impl(context):
       assert context.browser.title == "PyPI · The Python Package Index"
