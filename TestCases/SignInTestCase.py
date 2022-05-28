import time
import unittest
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
from Common.SetUp.SetUpFile import SetUpClass


class AmazonSignInTC(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)

    def test_login_TC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_userName_field()
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.press_keep_me_singed_in_checkbox()
        self.passwordPage.press_sing_in_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
