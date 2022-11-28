import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def change_window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def open_browser(change_window_size):
    base_url = 'https://google.com'
    browser.open(base_url)


def test_google_result(open_browser):
    browser.element('[id="L2AGLb"]').press_enter()
    browser.element('[name="q"]').should(be.blank).type('selene git').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))

search_query_negative = 'Jhbhfgvkdjfvjdlfvkndf'
search_result_negative = 'По запросу - {search_query_negative} - ничего не найдено.'

def test_negative_google_result(open_browser):
    browser.element('[name="q"]').should(be.blank).type('Jhbhfgvkdjfvjdlfvkndf').press_enter()
    browser.element('[id="rcnt"]').should(have.text('По запросу Jhbhfgvkdjfvjdlfvkndf ничего не найдено.'))
