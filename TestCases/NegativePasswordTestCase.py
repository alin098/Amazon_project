import time
import unittest
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
from Common.SetUp.SetUpFile import SetUpClass
from Common.PersonalVariables.PersonalVariablesFile import *


class NegativePasswordTC(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)

    def test_negative_password_TC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_userName_field()
        self.loginPage.press_continue_button()
        message = self.passwordPage.validate_password_page_invalid_functionality().text
        self.assertEqual(message, errorMessage)
        print("Your password was incorrect.")

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
