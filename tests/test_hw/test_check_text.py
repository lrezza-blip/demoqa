from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.elements_page import ElementsPage

def test_footer_text():
    driver = webdriver.Chrome()
    base_url = 'https://demoqa.com/'

    try:
        driver.get(base_url)
        footer_text = driver.find_element(By.CSS_SELECTOR, "footer").text
        expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

        if footer_text == expected_text:
            print('Тест пройден')
        else:
            print(f"Получено: '{footer_text}'")

    except NoSuchElementException:
        print('не найден!')

    finally:
        driver.quit()

def test_elements_page_text():
    driver = webdriver.Chrome()
    base_url = 'https://demoqa.com/elements'

    try:
        driver.get(base_url)
        center_text = driver.find_element(By.CSS_SELECTOR, '.main-header').text
        assert center_text == 'Please select an item from left to start practice.'
        print('Тест пройден')

    except NoSuchElementException:
        print('не найден!')

    finally:
        driver.quit()



def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()