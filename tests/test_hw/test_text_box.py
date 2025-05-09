from selenium.webdriver.common.by import By
from pages.text_box import TextBox


def test_text_box(browser):
    test_text_box_page = TextBox(browser)
    test_text_box_page.visit()

    full_name = 'Tester Name'
    current_address = '123 Test Street'

    browser.find_element(By.ID, 'userName').send_keys(full_name)
    browser.find_element(By.ID, 'currentAddress').send_keys(current_address)

    submit_button = browser.find_element(By.ID, 'submit')
    test_text_box_page.scroll_to_element(submit_button)
    submit_button.click()

    output_text = browser.find_element(By.CSS_SELECTOR, '#output').text

    assert full_name in output_text, f"Expected: '{full_name}' got: '{output_text}'"
    assert current_address in output_text, f"Expected: '{current_address}' got: '{output_text}'"

