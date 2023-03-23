from helpers.model import app
from helpers.model.pages import search, toolbar, settings


def test_open_settings():
    app.given_opened()

    toolbar.tap_on_menu()
    toolbar.move_to_settings()

    settings.assert_settings_was_opened()


def test_open_language_settings():
    app.given_opened()

    toolbar.tap_on_menu()
    toolbar.move_to_settings()
    settings.open_language_settings()

    settings.assert_language_settings_was_opened()


def test_add_new_language():
    app.given_opened()

    toolbar.tap_on_menu()
    toolbar.move_to_settings()
    settings.open_language_settings()
    settings.open_language_list()
    settings.tap_on_search_field()
    settings.find_language('Spanish')
    settings.choose_language()

    settings.assert_language_was_added()
