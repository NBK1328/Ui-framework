import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",  
        help="Set browser language (forced to 'en' if not specified)",
    )

@pytest.fixture(scope="function")
def browser(request):
    
    useLanguage = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': useLanguage})
   
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)

    yield browser
    browser.quit()