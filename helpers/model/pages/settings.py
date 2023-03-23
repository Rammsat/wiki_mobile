from selene import have, be
from selene.support.shared import browser
from allure import step as title


def open_language_settings():
    with title('Открыть настройки языка'):
        browser.element('«Wikipedia languages»').tap()


def open_language_list():
    with title('Открыть настройки языка'):
        browser.element('«ADD LANGUAGE»').tap()


def tap_on_search_field():
    with title('Нажать на поле поиска языка'):
        browser.element('#menu_search_language').tap()


def find_language(value):
    with title('Найти язык'):
        browser.element('#search_src_text').type(value)


def choose_language():
    with title('Выбрать язык'):
        browser.element('#localized_language_name').tap()


def assert_settings_was_opened():
    with title('Настройки открыты'):
        browser.element('«Settings»').should(be.visible)


def assert_language_settings_was_opened():
    with title('Настройки языка открыты'):
        browser.element('«Wikipedia languages»').should(be.visible)


def assert_language_was_added():
    with title('Язык добавлен'):
        browser.element('«ES»').should(be.visible)
