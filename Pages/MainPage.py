from Locators.locatorsfile import *
from Common.CustomFind.FindElement import FindElement
from selenium.webdriver.common.keys import Keys
from Common.PersonalVariables.PersonalVariablesFile import *

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_cart_button(self):
        cartButton = self.findElement.find(*cartPressButtonLocator)
        cartButton.click()

    def press_home_page_button(self):
        homeButton = self.findElement.find(*homeButtonLocator)
        homeButton.click()

    def fill_search_field(self):
        searchField = self.findElement.find(*searchFieldLocator)
        searchField.clear()
        searchField.send_keys(*searchProduct)

    def press_search_button(self):
        searchButton = self.findElement.find(*searchButtonLocator)
        searchButton.click()

    def sign_out_button(self):
        accountAndLists = self.findElement.find(*accountAndListsLocator)
        accountAndLists.send_keys(Keys.ENTER)
        signOut = self.findElement.find(*signOutLocator)
        signOut.click()
