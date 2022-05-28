import time
import unittest
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
from Common.SetUp.SetUpFile import SetUpClass
from Pages.MainPage import MainPageClass
from Pages.SearchResultPage import SearchResultPageClass
from Pages.ItemsPage import ItemsPageClass


class AddProduct(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.mainPage = MainPageClass(self.driver)
        self.searchPage = SearchResultPageClass(self.driver)
        self.itemsPage = ItemsPageClass(self.driver)

    def test_LoginTC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_userName_field()
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.press_keep_me_singed_in_checkbox()
        self.passwordPage.press_sing_in_button()

        self.mainPage.press_home_page_button()
        self.mainPage.fill_search_field()
        self.mainPage.press_search_button()
        self.searchPage.open_third_product()
        self.itemsPage.press_add_to_cart_button()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
