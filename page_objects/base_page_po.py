import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage (unittest.TestCase):

    def __init__(self, driver):
        super(BasePage,self).__init__(driver)
    #
    # def setUp(self):
    #     # create a new Chrome session
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(30)
    #     self.driver.maximize_window()
    #
    #     # navigate to Redmine Login  page
    #     # MACBOOK
    #     # self.driver.get("http://192.168.64.2/login"
    #     # DELL BSF
    #     self.driver.get("http://localhost/redmine/login")
    #
    # def tearDown(self):
    #     # close the browser window
    #     self.driver.quit()

