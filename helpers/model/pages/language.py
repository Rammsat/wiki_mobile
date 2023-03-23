from selene import be
from selene.support.shared import browser
from allure import step as title


def open_language_page():
    with title('Открыть страницу смены языка'):
        browser.element('#page_language').tap()


def tap_on_search_field():
    with title('Нажать на поле поиска языка'):
        browser.element('#menu_search_language').tap()


def find_language(value):
    with title('Найти язык'):
        browser.element('#search_src_text').type(value)


def choose_language():
    with title('Выбрать язык'):
        browser.element('#localized_language_name').tap()


def assert_language_was_found():
    with title('Язык был найден'):
        browser.element('«Russian»').should(be.visible)


def assert_language_page_was_opened():
    with title('Страница выбора языка открыта'):
        browser.element('«Other languages»').should(be.visible)
