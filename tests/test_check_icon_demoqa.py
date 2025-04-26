from pages.demoqa import DemoQa
import time

def test_check_icon(browser):
    demo_qa_page = DemoQa(browser)
    time.sleep(3)
    demo_qa_page.visit()
    demo_qa_page.click_on_the_icon()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()

    # browser.get("https://demoqa.com/")
    #
    # icon = browser.find_element(By.CSS_SELECTOR,'header > a > img')
    # if icon is None:
    #     print('элемент не найден')
    # else:
    #     print('элемент найден')


