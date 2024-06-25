from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
