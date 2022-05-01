from Locators.locatorsfile import *

class LoginPageClass():
    def __init__(self, driver):
        self.driver = driver

    def fill_userName_field(self, text):
         userName = self.driver.find_element(*userNameLocator)
         userName.clear()
         userName.send_keys(text)

    def press_continue_button(self):
        continueButton = self.driver.find_element(*continueButtonLocator)
        continueButton.click()












