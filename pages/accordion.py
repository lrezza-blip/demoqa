from components.components import WebElement
from pages.base_page import BasePage

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section1_heading = WebElement(driver, '#section1Heading')
        self.section1_content = WebElement(driver, '#section1Content > p')
        self.section2_content1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section2_content2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section3_content = WebElement(driver, '#section3Content > p')