import time
from Locators.locatorsfile import *
from Common.CustomFind.FindElement import FindElement

class ShoppingCartClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def delete_shopping_cart_first_item(self):
        firstItem = self.findElement.find(*firstItemLocator)
        firstItem.click()

    def delete_all_items_in_shopping_cart(self):
        cartCountElement = self.findElement.find(*pageCardCountLocator)
        numberOfAllProdacts = int(cartCountElement.text)
        while numberOfAllProdacts > 0:
            numberOfAllProdacts -= 1
            self.delete_shopping_cart_first_item()
            time.sleep(2)
