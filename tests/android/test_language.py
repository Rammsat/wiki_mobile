from helpers.model import app
from helpers.model.pages import search, language


def test_open_language_page():
    app.given_opened()

    search.tap_on_search_field()
    search.find_article('Selene')
    search.open_article()
    language.open_language_page()

    language.assert_language_page_was_opened()


def test_find_language():
    app.given_opened()

    search.tap_on_search_field()
    search.find_article('Selene')
    search.open_article()
    language.open_language_page()
    language.tap_on_search_field()
    language.find_language('russian')

    language.assert_language_was_found()


def test_change_language():
    app.given_opened()

    search.tap_on_search_field()
    search.find_article('Selene')
    search.open_article()
    language.open_language_page()
    language.tap_on_search_field()
    language.find_language('russian')
    language.choose_language()

    search.assert_article_was_opened()
