import time
import unittest
from Common.SetUp.SetUpFile import SetUpClass
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
from Pages.MainPage import MainPageClass
from Common.PersonalVariables.PersonalVariablesFile import *


class AmazonSignInTC(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.mainPage = MainPageClass(self.driver)

    def test_LoginTC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_userName_field()
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.press_keep_me_singed_in_checkbox()
        self.passwordPage.press_sing_in_button()

        self.mainPage.sign_out_button()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
