import time

from Locators.locatorsfile import *


class ShoppingCartClass():
    def __init__(self, driver):
        self.driver = driver

    def delete_shopping_cart_first_item(self):
        firstItem = self.driver.find_element(*firstItemLocator)
        firstItem.click()

    def delete_all_items_in_shopping_cart(self):
        cartCountElement = self.driver.find_element(*pageCardCountLocator)
        numberOfAllProdacts = int(cartCountElement.text)
        while numberOfAllProdacts > 0:
            numberOfAllProdacts -= 1
            self.delete_shopping_cart_first_item()
            time.sleep(3)
