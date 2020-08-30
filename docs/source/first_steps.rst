First steps with Elemental
==========================


Step 1. Install
---------------

Elemental can be installed with ``pip``::

    $ pip install elemental


Step 2. Start the browser
-------------------------

Getting a browser to drive your automation is this easy:

.. code:: python

   >>> import elemental
   >>> browser = elemental.Browser()


This will give you the default Firefox browser.

For information about configuring the default browser and using a custom
browser, see the :doc:`Browser </browser>` reference.


.. admonition:: Geckodriver required

   Note that `Mozilla's geckodriver <https://github.com/mozilla/geckodriver>`_
   must be installed and available on PATH to use the default Selenium
   webdriver.


Step 3. Use the browser
-----------------------

Now do whatever you like with it. How about a web search?

.. code:: python

   >>> browser.visit("https://duckduckgo.com")
   >>> placeholder = "Search the web without being tracked"
   >>> browser.get_input(placeholder=placeholder).fill("python news")
   >>> browser.get_input(id="search_button_homepage").click()


Enjoy your search results!
