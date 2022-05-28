import time
import unittest
from Pages.SignInPage.LoginPage import LoginPageClass
from Common.SetUp.SetUpFile import SetUpClass


class NegativeLoginTC(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)

    def test_negative_login_TC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_userName_field()
        self.assertEqual(self.loginPage.validate_login_page_invalid_functionality().text , 'We cannot find an account with that mobile number')
        print("Your username was incorrect")

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
