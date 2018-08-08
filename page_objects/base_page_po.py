import unittest
import time
from selenium import webdriver


class BasePage (unittest.TestCase):

    def __init__(self, driver):
         super(BasePage, self).__init__(driver)


    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to Redmine Login  page
        self.driver.get("http://192.168.64.2/login")



    def tearDown(self):
        # wait 5 seconds on Home after Login
        time.sleep(3)

        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)