from page_objects.login_po import Login
from selenium.webdriver.common.by import By
import unittest
from page_objects.base_page_po import BasePage




class Home(BasePage):

    def __init__(self, driver):
        self.driver = driver

        # Transformo locators en elementos
        self.lbl = self.driver.find_element_by_xpath("//*[@id='content']/h2")

    def navigate_to_projects(self):
        # get the PROJECT link
        self.search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
        self.search_field_menu_projects.click()























# #y además puso esto el Cris
#
#     def __init__(self, driver):
#         super(Home, self).__init__(driver)
#
#
#
#     def click_on_link(self):
#         we = self.driver.find_element(self._lnk_home_loc[0], self._lnk_home_loc[1])

