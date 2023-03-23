import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import helpers.utils.selene.patch_selector_strategy  # noqa
    import helpers.utils.selene.patch_element_mobile_commands  # noqa
