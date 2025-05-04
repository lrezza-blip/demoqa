from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()

    assert modal_elements.check_count_elements(count=35)

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    browser.refresh()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert browser.current_url == 'https://demoqa.com/modal-dialogs'
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
