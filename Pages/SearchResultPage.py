from Common.CustomFind.FindElement import FindElement
from Locators.locatorsfile import *

class SearchResultPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def open_third_product(self):
        thirdProduct = self.findElement.find(*thirdProductLocator)
        thirdProduct.click()
