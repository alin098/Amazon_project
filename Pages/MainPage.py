from Locators.locatorsfile import *

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver

    def press_cart_button(self):
        cartButton = self.driver.find_element(*cartPressButtonLocator)
        cartButton.click()




