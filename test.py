from selenium.webdriver.common.by import By
from fill import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, get_driver):
            text_box_page = TextBoxPage(get_driver, 'https://automationintesting.online')
            text_box_page.open()
            text_box_page.fill_all_fields()
            header = get_driver.find_element(By.CSS_SELECTOR, 'div[class="col-sm-5"]')
            assert header.text == 'Message\n\nSubmit'
