Raw Selenium
============

You can use Elemental and still access the full power of Selenium any time you
need it.


Selenium webdriver
------------------

Every instance of Elemental's ``Browser`` class has a ``selenium_webdriver``
property which provides an instance of Selenium's WebDriver.

It can be used like this:

.. code :: python

   import elemental

   browser = elemental.Browser()
   browser.visit("https://pypi.org")

   # Elemental doesn't provide a way to get cookies, so use the Selenium
   # webdriver's get_cookies() method.
   cookies = browser.selenium_webdriver.get_cookies()
   print(cookies)


Selenium webelement
-------------------

Every instance of Elemental's ``Element`` class has a ``selenium_webdriver``
property which provides an instance of Selenium's WebDriver.

Every instance of Elemental's ``Element`` class also has a
``selenium_webelement`` property which provides an instance of the Selenium
WebElement which corresponds to its HTML element.

It can be used like this:

.. code :: python

   import elemental

   browser = elemental.Browser()
   browser.visit("https://pypi.org")
   logo = browser.get_element(class_name="site-header__logo")

   # Elemental doesn't provide a way to get the element's size, so use the
   # Selenium webelement's size property.
   logo_size = logo.selenium_webelement.size
   print(logo_size)
