#test_webtables.py
from pages.webtables_page import WebTables

def test_webtables(browser):
    page = WebTables(browser)
    page.visit()

    page.wait_and_click(page.Add_Button)
    assert page.dialog_open()

    page.wait_and_click(page.Submit)
    assert len(browser.find_elements(*page.Error)) > 0

    new_record = {
        "firstName": "Tester",
        "lastName": "Testerok",
        "userEmail": "test@test.te",
        "age": "99",
        "salary": "111",
        "department": "Fashion",
    }

    page.fill_form(new_record)
    page.wait_and_click(page.Submit)

    assert page.dialog_closed()
    assert page.record_in_table(new_record)

    page.perform_action_on_row(new_record, "edit")

    assert page.dialog_open()
    for field, locator in page.Fields.items():
        input_field = page.browser.find_element(*locator)
        assert input_field.get_attribute("value") == new_record[field]

    updated_record = new_record.copy()
    updated_record["firstName"] = "Masha"
    page.fill_form(updated_record)
    page.wait_and_click(page.Submit)

    assert page.dialog_closed()
    assert page.record_in_table(updated_record)

    page.perform_action_on_row(updated_record, "delete")

    assert not page.record_in_table(updated_record)