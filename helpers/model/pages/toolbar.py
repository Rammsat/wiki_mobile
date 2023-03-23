from selene import have, be
from selene.support.shared import browser
from allure import step as title


def tap_on_menu():
    with title('Нажать на кнопку "Меню"'):
        browser.element('#menu_icon').tap()


def move_to_settings():
    with title('Перейти в настройки'):
        browser.element('#main_drawer_settings_container').tap()
