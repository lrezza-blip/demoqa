import time
from pages.alerts import Alerts

def test_timer_alert(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()

    assert alerts_page.alertButton.exist()

    alerts_page.alertButton.click()
    time.sleep(2)

    alert = browser.switch_to.alert
    assert alert is not None
    alert.accept()

