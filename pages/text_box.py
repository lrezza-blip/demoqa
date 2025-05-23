from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):

    def __init__(self,driver):
      self.base_url = 'https://demoqa.com/text-box'
      super().__init__(driver,self.base_url)

      self.name = WebElement(driver, '#userName')
      self.submit = WebElement(driver, '#submit')

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)