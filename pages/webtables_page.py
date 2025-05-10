#webtables_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebTables:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://demoqa.com/webtables'

    Add_Button = (By.ID, "addNewRecordButton")
    Dialog_box = (By.CLASS_NAME, "modal-content")
    Edit = (By.CSS_SELECTOR, ".action-buttons span[title='Edit']")
    Submit = (By.ID, "submit")
    Rows = (By.CLASS_NAME, "rt-tr-group")
    Delete = (By.CSS_SELECTOR, ".action-buttons span[title='Delete']")
    Error = (By.CSS_SELECTOR, "input:invalid")

    Fields = {
        "firstName": (By.ID, "firstName"),
        "lastName": (By.ID, "lastName"),
        "userEmail": (By.ID, "userEmail"),
        "age": (By.ID, "age"),
        "salary": (By.ID, "salary"),
        "department": (By.ID, "department"),
    }


    def visit(self):
        return self.browser.get(self.base_url)

    def wait_for_element(self, locator):
        return WebDriverWait(self.browser,10).until(EC.presence_of_element_located(locator))

    def wait_and_click(self, locator):
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def fill_form(self, data):
        for field, locator in self.Fields.items():
            input_field = self.wait_for_element(locator)
            input_field.clear()
            input_field.send_keys(data[field])

    def get_rows(self):
        rows = self.browser.find_elements(*self.Rows)
        return [row.text for row in rows if row.text.strip()]

    def record_in_table(self, data):
        rows = self.get_rows()
        return any(
            data["firstName"] in row and data["lastName"] in row and data["userEmail"] in row
            for row in rows
        )

    def dialog_open(self):
        try:
            self.wait_for_element(self.Dialog_box)
            return True
        except:
            return False

    def dialog_closed(self):
        try:
            WebDriverWait(self.browser,10).until(EC.invisibility_of_element(self.Dialog_box))
            return True
        except:
            return False

    def perform_action_on_row(self, data, action):
        rows = self.browser.find_elements(*self.Rows)
        for row in rows:
            if (
                    data["firstName"] in row.text
                    and data["lastName"] in row.text
                    and data["userEmail"] in row.text
            ):
                if action == "edit":
                    row.find_element(By.CSS_SELECTOR, "span[title='Edit']").click()
                elif action == "delete":
                    row.find_element(By.CSS_SELECTOR, "span[title='Delete']").click()
                break
        else:
            raise ValueError