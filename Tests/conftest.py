import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["firefox"], scope='class')
def init_driver(request):
    if request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("browser.link.open_newwindow", 1)
        web_driver = webdriver.Firefox(options=firefox_options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
