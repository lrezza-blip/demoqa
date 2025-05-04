from pages.base_page import BasePage

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.buttons_submenu = (By.CSS_SELECTOR, ".btn")


    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".btn")

    def check_count_elements(self,count:int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False
