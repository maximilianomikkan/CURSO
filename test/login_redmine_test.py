#+import unittest
from page_objects.base_page_po import BasePage
from features.environment import Environment
from page_objects.login_po import Login
#from selenium import webdriver


class Login():
    print("Hola0")
    def __init__(self, driver):
        self.driver = driver
        print("Hola1")
        env = Environment()
        env.setUp()


        login = Login()
        login.login_redmine("miuser", "mipass")
        #home = login.login_redmine(self, "user", "pass")
        #assert home.txf_home_loc.text == "Home"
        print("Hola2")

        env.tearDown()
