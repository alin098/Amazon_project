from Common.CustomFind.FindElement import FindElement
from Locators.locatorsfile import *
from Common.PersonalVariables.PersonalVariablesFile import *


class LoginPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def fill_userName_field(self):
        userName = self.findElement.find(*userNameLocator)
        userName.clear()
        userName.send_keys(*login)

    def press_continue_button(self):
        continueButton = self.findElement.find(*continueButtonLocator)
        continueButton.click()

    def validate_login_page_invalid_functionality(self):
        userName = self.findElement.find(*userNameLocator)
        userName.clear()
        userName.send_keys(*wrongLogin)
        self.press_continue_button()
        errorMessage = self.findElement.find(*userNameErrorLocator)
        return errorMessage
