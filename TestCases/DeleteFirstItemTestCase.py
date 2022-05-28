import time
import unittest
from Common.SetUp.SetUpFile import SetUpClass
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
from Pages.ShoppingCartPage import ShoppingCartClass
from Pages.MainPage import MainPageClass


class DeleteFirstItemClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.shoppingPage = ShoppingCartClass(self.driver)
        self.mainPage = MainPageClass(self.driver)

    def test_DeleteFirstItemTC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_userName_field()
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.press_keep_me_singed_in_checkbox()
        self.passwordPage.press_sing_in_button()

        self.mainPage.press_cart_button()
        self.shoppingPage.delete_shopping_cart_first_item()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
