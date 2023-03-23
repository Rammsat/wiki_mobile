from selene import have, be
from selene.support.shared import browser
from allure import step as title


def tap_on_search_field():
    with title('Нажать на строку поиска'):
        browser.element('Search Wikipedia').tap()


def find_article(value):
    with title('Найти статью'):
        browser.element('#search_src_text').type(value)


def open_article():
    with title('Открыть статью'):
        browser.element('«Ancient Greek goddess of the Moon»').tap()


def assert_article_was_opened():
    with title('Статья открыта'):
        browser.element('#view_page_header_image').should(be.visible)


def assert_successful_search():
    with title('Поиск выполнен успешно'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))


def assert_search_without_results():
    with title('Поиск не выдал результата'):
        browser.all('#page_list_item_title').should(have.size(0))
