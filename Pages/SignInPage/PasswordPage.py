import time
from Locators.locatorsfile import *
from Common.CustomFind.FindElement import FindElement
from Common.PersonalVariables.PersonalVariablesFile import *

class PasswordPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def fill_password_field(self):
        passwordName = self.findElement.find(*passwordNameLocator)
        passwordName.clear()
        passwordName.send_keys(*password)
        time.sleep(3)

    def press_keep_me_singed_in_checkbox(self):
        keepSingedIn = self.findElement.find(*keepSingedInLocator)
        keepSingedIn.click()

    def press_sing_in_button(self):
        signIn = self.findElement.find(*signInLocator)
        signIn.click()

    def validate_password_page_invalid_functionality(self):
        passwordName = self.findElement.find(*passwordNameLocator)
        passwordName.clear()
        passwordName.send_keys(*wrongPassword)
        time.sleep(3)
        self.press_sing_in_button()
        errorMessage = self.findElement.find(*passwordNameErrorLocator)
        return errorMessage
