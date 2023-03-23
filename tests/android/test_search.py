from helpers.model import app
from helpers.model.pages import search


def test_successful_search():
    app.given_opened()

    search.tap_on_search_field()
    search.find_article('Selene')

    search.assert_successful_search()


def test_search_without_results():
    app.given_opened()

    search.tap_on_search_field()
    search.find_article('ghdfkjgd')

    search.assert_search_without_results()


def test_open_an_article():
    app.given_opened()

    search.tap_on_search_field()
    search.find_article('Selene')
    search.open_article()

    search.assert_article_was_opened()
