import time
from pages.modal_dialogs import ModalDialogs

def test_small_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()
    assert modal_dialogs_page.small_modal_button.exist()

    modal_dialogs_page.small_modal_button.click()
    time.sleep(2)
    assert modal_dialogs_page.small_modal.exist()

    modal_dialogs_page.small_modal_close_button.click()
    time.sleep(2)
    assert not modal_dialogs_page.small_modal.exist()


def test_large_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()
    assert modal_dialogs_page.large_modal_button.exist()

    modal_dialogs_page.large_modal_button.click()
    time.sleep(2)
    assert modal_dialogs_page.large_modal.exist()

    modal_dialogs_page.large_modal_close_button.click()
    time.sleep(2)
    assert not modal_dialogs_page.large_modal.exist()

