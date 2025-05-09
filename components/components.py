from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.common.keys import  Keys

class WebElement:
    def __init__(self,driver,locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script('arguments[0].click();', self.find_element())

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        return self.find_element().is_displayed()

    def get_text(self):
        try:
            return str(self.find_element().text)
        except NoSuchElementException:
            return False
        return True

    def check_count_elements(self,count:int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    def get_dom_attribute(self,name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        if self.locator_type == 'name':
            return By.NAME
        if self.locator_type == 'xpath':
            return By.XPATH
        if self.locator_type == 'css':
            return By.CSS
        if self.locator_type == 'class':
            return By.CLASS_NAME
        if self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('locator type' + self.locator_type + 'not correct')
        return False

    def scroll_to_element(self):
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);',
            self.find_element()
        )

    # home task
class Comp:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def get_text(self):
        try:
            return str(self.find_element().text)
        except NoSuchElementException:
            return False
        return True



