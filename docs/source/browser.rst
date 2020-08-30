Browser
=======

The ``Browser`` class provides the browser which drives Elemental.


The Browser class
-----------------

.. function::
   Browser(selenium_webdriver=None, headless=False)

*Parameters*
  :selenium_webdriver:
    :class:`Selenium webdriver, optional` The webdriver being used to drive the
    browser. Default is a Firefox webdriver.
  :headless:
    :class:`bool, optional` Whether the default webdriver will run in headless
    mode. Has no effect if the default webdriver is not used. Default is False.

*Example: Default browser*
  .. code-block:: python

     import elemental

     browser = elemental.Browser()
     browser.visit("https://pypi.org/project/elemental/")

*Example: Headless default browser*
  .. code-block:: python

     import elemental

     browser = elemental.Browser(headless=True)
     browser.visit("https://pypi.org/project/elemental/")


Modifying the default browser
-----------------------------

The ``Browser`` class has a ``selenium_webelement`` property which is the
underlying Selenium webdriver.

Use that to modify the default browser when necessary.

For example, to set window size of the default webdriver:

.. code-block:: python

   import elemental

   browser = elemental.Browser(headless=True)
   browser.selenium_webdriver.set_window_size(1920, 1080)

   browser.visit("https://pypi.org/project/elemental/")


Bring-your-own browser
----------------------

To use your own browser rather than the default browser, instantiate
``Browser`` with a Selenium WebDriver instance as the only argument.

For example:

.. code-block:: python

   import elemental
   import selenium
   from selenium.webdriver.firefox import options as firefox_options

   options = firefox_options.Options()
   options.headless = True
   selenium_webdriver = selenium.webdriver.Firefox(
       executable_path="geckodriver",
       options=options,
   )

   browser = elemental.Browser(selenium_webdriver)
