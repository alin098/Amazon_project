from Locators.locatorsfile import *


class PasswordPageClass():
    def __init__(self, driver):
        self.driver = driver

    def fill_password_field(self, text):
        passwordName = self.driver.find_element(*passwordNameLocator)
        passwordName.clear()
        passwordName.send_keys(text)

    def press_keep_me_singed_in(self):
        keepSingedIn = self.driver.find_element(*keepSingedInLocator)
        keepSingedIn.click()

    def sing_in_field(self):
        signIn = self.driver.find_element(*signInLocator)
        signIn.click()





