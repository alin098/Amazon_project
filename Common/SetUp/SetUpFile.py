from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SetUpClass():
    def generalSetUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
