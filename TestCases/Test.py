import time
import unittest
from selenium import webdriver
from Pages.LoginPage import LoginPageClass
from Pages.PasswordPage import PasswordPageClass
from Pages.MainPage import MainPageClass
from Pages.ShoppingCartPage import ShoppingCartClass


class AmazonLoginPageTC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.mainPage = MainPageClass(self.driver)
        self.shoppingPage = ShoppingCartClass(self.driver)


    def test_LoginTC(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.loginPage.fill_userName_field("+37477900413")
        self.loginPage.press_continue_button()
        time.sleep(3)
        self.passwordPage.fill_password_field("1234567/*-")
        self.passwordPage.press_keep_me_singed_in()
        time.sleep(3)
        self.passwordPage.sing_in_field()
        time.sleep(3)
        self.mainPage.press_cart_button()
        time.sleep(3)
        self.shoppingPage.delete_shopping_cart_first_item()
        time.sleep(3)
        self.shoppingPage.delete_all_items_in_shopping_cart()
        time.sleep(3)

    def tearDown(self):
        time.sleep(1)
        self.driver.close()



