from locator import TextBoxLocators
from page import BasePage
from generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        email = person_info.email
        phone = person_info.phone
        subject = person_info.subject
        message = person_info.message
        self.element_is_present(self.locators.NAME).send_keys(name)
        self.element_is_present(self.locators.EMAIL).send_keys(email)
        self.element_is_present(self.locators.PHONE).send_keys(phone)
        self.element_is_present(self.locators.SUBJECT).send_keys(subject)
        self.element_is_present(self.locators.MESSAGE).send_keys(message)
        self.element_is_present(self.locators.SUBMIT).click()
