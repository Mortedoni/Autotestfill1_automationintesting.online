from selenium.webdriver.common.by import By


class TextBoxLocators:
    NAME = (By.CSS_SELECTOR, 'input[id="name"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="email"]')
    PHONE = (By.CSS_SELECTOR, 'input[id="phone"]')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subject"]')
    MESSAGE = (By.CSS_SELECTOR, 'textarea[id="description"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submitContact"]')
