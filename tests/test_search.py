import pytest
from selene import browser, be, have


@pytest.fixture(scope='function')
def browser_management():
     browser.config.driver_name = 'chrome'
     browser.config.base_url = 'https://google.com'
     browser.config.window_width = 1920 #ширина окна браузера
     browser.config.window_height = 1080 #высота окна браузера


def test_search_valid():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.quit()


def test_search_no_valid():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ddd786&&&5459056hyjdyktykstyky##').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу ddd786&&&5459056hyjdyktykstyky## ничего не найдено'))
    browser.quit()