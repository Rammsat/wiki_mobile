from selene import be
from selene.support.shared import browser
from allure import step as title


def given_opened():
    if browser.element('#fragment_onboarding_skip_button').matching(be.visible):
        with title('Закрыть начальную настройку приложения'):
            browser.element('#fragment_onboarding_skip_button').tap()
