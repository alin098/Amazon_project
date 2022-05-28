from Common.CustomFind.FindElement import FindElement
from Locators.locatorsfile import *

class ItemsPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_add_to_cart_button(self):
        addToCartButton = self.findElement.find(*addToCartButtonLocator)
        addToCartButton.click()
