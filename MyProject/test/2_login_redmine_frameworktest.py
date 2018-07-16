import unittest
import time
from selenium import webdriver


class SearchTests(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to Redmine Login  page
        self.driver.get("http://192.168.64.2/login")


    def test_search_by_id(self):
        # get the USERNAME textbox
        self.search_field_username = self.driver.find_element_by_id("username")
        self.search_field_username.clear()

        # get the PASSWORD textbox
        self.search_field_password = self.driver.find_element_by_id("password")
        self.search_field_password.clear()

        # enter USERNAME keyword
        self.search_field_username.send_keys("maximilianomikkan")

        # enter PASSWORD keyword
        self.search_field_password.send_keys("abc123")

        # get the LOGIN button
        self.search_field_login = self.driver.find_element_by_name("login")
        self.search_field_login.click()


    def tearDown(self):
        # wait 5 seconds on Home after Login
        time.sleep(5)



        # close the browser window
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)
